import argparse
import pandas as pd

"""
把 woocommerce 的商品数据导出来的 CSV 进行转化
"""
def transform_wc_data(input_file, output_file):
    # Load the WooCommerce exported product data
    wc_data = pd.read_csv(input_file)

    # Define all the desired columns for the new format, even if some don't exist in the input file
    new_columns = [
        "ParentSKU", "SKU", "DealTitle", "Price", "RRP", "Stock", "UnlimitedStock",
        "GTIN", "MPN", "Description", "Specification", "Brand", "Condition",
        "CategoryID", "SearchKeywords", "ShippingWeight", "ShippingLength",
        "ShippingHeight", "ShippingWidth", "ShippingCostCategory", "FlatRate",
        "FreightSchemeID", "DeliveryTime", "MaxDaysForDelivery", "FastDispatch",
        "OptionName_1", "OptionValue_1", "OptionName_2", "OptionValue_2",
        "OptionName_3", "OptionValue_3", "ImageURL_1", "ImageURL_2", "ImageURL_3",
        "ImageURL_4", "ImageURL_5", "ImageURL_6", "ImageURL_7", "ImageURL_8",
        "ImageURL_9", "ImageURL_10", "ImageURL_11", "ImageURL_12", "ImageURL_13",
        "ImageURL_14", "ImageURL_15", "ImageURL_16", "ImageURL_17", "ImageURL_18",
        "ImageURL_19", "ImageURL_20", "ImageURL_21", "ImageURL_22", "ImageURL_23",
        "ImageURL_24", "ImageURL_25", "ImageURL_26", "ImageURL_27", "ImageURL_28",
        "ImageURL_29", "ImageURL_30"
    ]

    # Create a new DataFrame with the columns listed, populating with default or transformed values
    wc_data_transformed = pd.DataFrame(columns=new_columns)

    # Mapping relevant columns
    wc_data_transformed["ParentSKU"] = wc_data["SKU"]
    wc_data_transformed["SKU"] = wc_data["SKU"]
    wc_data_transformed["DealTitle"] = wc_data["Name"]
    wc_data_transformed["Price"] = wc_data["Regular price"]
    wc_data_transformed["Description"] = wc_data["Description"]
    wc_data_transformed["Condition"] = "New"
    wc_data_transformed["Stock"] = wc_data["Stock"]
    wc_data_transformed["CategoryID"] = wc_data["Meta: my_deal_category_id"]
    wc_data_transformed["SearchKeywords"] = wc_data["Meta: search_keywords"]
    wc_data_transformed["ShippingWeight"] = wc_data["Weight (kg)"]
    wc_data_transformed["ShippingLength"] = wc_data["Length (cm)"]
    wc_data_transformed["ShippingWidth"] = wc_data["Width (cm)"]
    wc_data_transformed["ShippingHeight"] = wc_data["Height (cm)"]

    # TODO: 添加判断是否是否包邮
    wc_data_transformed["ShippingCostCategory"] = "Other"
    wc_data_transformed["FreightSchemeID"] = "2303"

    # Handling Image URLs (splitting multiple images if needed), max 10 images
    wc_data_transformed["ImageURL_1"] = wc_data["Images"].apply(lambda x: str(x).split(",")[0] if pd.notna(x) else "")
    wc_data_transformed["ImageURL_2"] = wc_data["Images"].apply(lambda x: str(x).split(",")[1] if pd.notna(x) and len(str(x).split(",")) > 1 else "")
    wc_data_transformed["ImageURL_3"] = wc_data["Images"].apply(lambda x: str(x).split(",")[3] if pd.notna(x) and len(str(x).split(",")) > 2 else "")
    wc_data_transformed["ImageURL_4"] = wc_data["Images"].apply(lambda x: str(x).split(",")[4] if pd.notna(x) and len(str(x).split(",")) > 3 else "")
    wc_data_transformed["ImageURL_5"] = wc_data["Images"].apply(lambda x: str(x).split(",")[5] if pd.notna(x) and len(str(x).split(",")) > 4 else "")
    wc_data_transformed["ImageURL_6"] = wc_data["Images"].apply(lambda x: str(x).split(",")[6] if pd.notna(x) and len(str(x).split(",")) > 5 else "")
    wc_data_transformed["ImageURL_7"] = wc_data["Images"].apply(lambda x: str(x).split(",")[7] if pd.notna(x) and len(str(x).split(",")) > 6 else "")
    wc_data_transformed["ImageURL_8"] = wc_data["Images"].apply(lambda x: str(x).split(",")[8] if pd.notna(x) and len(str(x).split(",")) > 7 else "")
    wc_data_transformed["ImageURL_9"] = wc_data["Images"].apply(lambda x: str(x).split(",")[9] if pd.notna(x) and len(str(x).split(",")) > 8 else "")
    wc_data_transformed["ImageURL_10"] = wc_data["Images"].apply(lambda x: str(x).split(",")[10] if pd.notna(x) and len(str(x).split(",")) > 9 else "")

    # Fill in empty columns with defaults, like empty strings or 0 for numerical columns
    wc_data_transformed.fillna("", inplace=True)

    # Export the transformed data to CSV with all specified columns
    wc_data_transformed.to_csv(output_file, index=False)
    print(f"Data successfully transformed and saved to {output_file}")


if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Transform WooCommerce exported data into the specified CSV format.")
    parser.add_argument("-f", "--file", required=True, help="Path to the WooCommerce exported CSV file")
    parser.add_argument("-o", "--output", required=True, help="Output file path for the transformed CSV")

    args = parser.parse_args()

    # Call the transformation function with the provided file paths
    transform_wc_data(args.file, args.output)

