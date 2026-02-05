def main():
    products = [
        ['toyota', 5200],
        ['honda', 6050],
        ['bmw', 15000],
        ['dodge', 9000],
        ['ford', 8000]
    ]
    
    print("Please select the car number:")
    for i, product in enumerate(products, 1):
        print(f"{i}- {product[0]} - {product[1]} SR")
    
    try:
        choice = int(input("please enter the car number:"))
        
        if 1 <= choice <= len(products):
            selected_product = products[choice - 1]
            product_name = selected_product[0]
            price = selected_product[1]
            
            tax = price * 0.15
            total_price = price + tax
            
            print(f"total price with tax: {total_price:.2f} SR")
            
        else:
            print("wrong number")
            
    except ValueError:
        print("the number must be integer")

if __name__ == "__main__":
    main()