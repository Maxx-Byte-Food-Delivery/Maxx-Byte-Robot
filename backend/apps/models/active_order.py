from django.db import models
from django.utils import timezone


class ActiveOrderStatus(models.TextChoices):
    PLACED = 'P', ('Placed')
    CONFIRMED = 'C', ('Confirmed')
    PREPAIRING = 'PRE', ("Preparing")
    LOCKED = 'L', ('Locked (No Edits)')
    OUT_FOR_DELIVERY = 'OFD', ('Out for Delivery')



class ActiveOrder(models.Model):
    """
    Represents an order that is still editable before dispatch.
    """

    user = models.IntegerField()  # Replace with FK if needed

    status = models.CharField(
        max_length=30,
        choices=ActiveOrderStatus.choices,
        default=ActiveOrderStatus.PLACED
    )

    # 📍 Delivery
    delivery_location = models.CharField(max_length=255)
    delivery_notes = models.TextField(blank=True, null=True)

    # 💰 Pricing
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    delivery_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # ⏱ Edit Control
    editable_until = models.DateTimeField(null=True, blank=True)

    # 🤖 Robot / Routing Hooks
    route_id = models.CharField(max_length=100, blank=True, null=True)
    estimated_delivery_time = models.DateTimeField(null=True, blank=True)

    # 🔄 Sync + lifecycle
    last_modified_by_user = models.BooleanField(default=True)
    version = models.PositiveIntegerField(default=1)  # optimistic locking

    # 📅 Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # -------------------------
    # 🧠 Business Logic Methods
    # -------------------------

    def is_editable(self):
        """
        Determines if the order can still be edited.
        """
        if self.status in [
            ActiveOrderStatus.PLACED,
            ActiveOrderStatus.CONFIRMED,
        ]:
            if self.editable_until:
                return timezone.now() <= self.editable_until
            return True
        return False

    def lock(self):
        """
        Locks the order (called when kitchen starts preparing).
        """
        self.status = ActiveOrderStatus.LOCKED
        self.save(update_fields=["status"])

    def increment_version(self):
        """
        Used for optimistic concurrency control.
        Prevents overwriting changes in real-time editing.
        """
        self.version += 1
        self.save(update_fields=["version"])

    def __str__(self):
        return f"ActiveOrder #{self.id} ({self.status})"