def main():
    print("💰 Money Management App 起動中...")
    print("収支を記録します。終了するには 'q' を入力してください。\n")

    records = []

    while True:
        category = input("カテゴリ（収入/支出）を入力: ")
        if category.lower() == 'q':
            break

        amount = input("金額を入力: ")
        if amount.lower() == 'q':
            break

        try:
            amount = float(amount)
        except ValueError:
            print("⚠️ 数字を入力してください。")
            continue

        records.append({"category": category, "amount": amount})
        print(f"✅ 記録しました: {category} - ¥{amount}\n")

    print("\n📊 記録されたデータ:")
    for record in records:
        print(f"- {record['category']}: ¥{record['amount']}")

if __name__ == "__main__":
    main()
