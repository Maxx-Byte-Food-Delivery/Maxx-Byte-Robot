export class CartModel {
    totalQty = 0;
    totalCost = 0;
    entries = new Map();

    constructor() {
        this.totalQty = 0;
        this.totalCost = 0;
        this.entries = new Map();
    }
}