export class CartEntry {
    name = "";
    price = 0;
    quantity = 0;

    constructor(name, price, quantity) {
        this.name = name;
        this.price = price;
        this.quantity = quantity;
    }
}