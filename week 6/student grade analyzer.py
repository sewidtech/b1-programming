import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def calculate_discount(category, tier):
    category_discounts = {
        "Electronics": 10,
        "Clothing": 15,
        "Books": 5,
        "Home": 12
    }

    tier_discounts = {
        "Premium": 5,
        "Standard": 0,
        "Budget": 2
    }

    return category_discounts.get(category, 0) + tier_discounts.get(tier, 0)



def process_products(input_file, output_file):
    try:
        products = []
        total_discount_amount = 0

        # Read input file
        with open(input_file, 'r') as f:
            for line_num, line in enumerate(f, 1):
                try:
                    parts = line.strip().split(",")

                    if len(parts) != 4:
                        logging.warning(f"Line {line_num}: Invalid format, skipping")
                        continue

                    name, price_str, category, tier = parts
                    base_price = float(price_str)

                    discount_pct = calculate_discount(category, tier)
                    discount_amt = base_price * (discount_pct / 100)
                    final_price = base_price - discount_amt

                    products.append({
                        "name": name,
                        "base_price": base_price,
                        "discount_pct": discount_pct,
                        "discount_amt": discount_amt,
                        "final_price": final_price
                    })

                    total_discount_amount += discount_amt

                except ValueError:
                    logging.error(f"Line {line_num}: Invalid price")
                    continue

        # Write output file
        with open(output_file, 'w') as f:
            f.write(f"{'Product Name':<30} {'Base Price':>12} {'Discount %':>12} "
                    f"{'Discount $':>12} {'Final Price':>12}\n")
            f.write("-" * 90 + "\n")

            for p in products:
                f.write(f"{p['name']:<30} "
                        f"${p['base_price']:>11.2f} "
                        f"{p['discount_pct']:>11.1f}% "
                        f"${p['discount_amt']:>11.2f} "
                        f"${p['final_price']:>11.2f}\n")

        # Summary
        avg_discount = total_discount_amount / len(products) if products else 0

        print("\nProcessing Complete!")
        print(f"Total products processed: {len(products)}")
        print(f"Average discount amount: ${avg_discount:.2f}")
        print(f"Report saved to: {output_file}")

    except FileNotFoundError:
        print(f"ERROR: Could not find file '{input_file}'")

    except PermissionError:
        print(f"ERROR: Permission denied writing to '{output_file}'")

    except Exception as e:
        print(f"Unexpected error: {e}")



if __name__ == "__main__":
    process_products("product.txt", "pricing_report.txt")
