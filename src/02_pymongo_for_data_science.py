
# ⏳ 3. PyMongo for Data Science

'''
MongoDB offers numerous features that are valuable to developers; however, a data scientist's primary focus will be on wrangling and munging data. It may or may not be desirable to perform all data munging within Pandas; for a large, distributed database, it could be essential to conduct aggregation in MongoDB.

In the following, we will examine test data from a store for training purposes using an introductory command.
'''

## 1. Insert: Create a collection and insert data

	collection = client["datascience_db"]["sales_data"] # Connecting to the "sales_data" collection in the "datascience_db" database.
	collection.drop()  # Clean collection if it already exists

	# Initial sales data
	sales_data = [
		{"product": "Laptop", "price": 1500, "quantity": 4, "category": "Electronics", "region": "Europe"},
		{"product": "Smartphone", "price": 850, "quantity": 10, "category": "Electronics", "region": "Asia"},
		{"product": "Tablet", "price": 420, "quantity": 7, "category": "Electronics", "region": "America"},
		{"product": "Desk", "price": 320, "quantity": 5, "category": "Furniture", "region": "Europe"},
		{"product": "Chair", "price": 150, "quantity": 12, "category": "Furniture", "region": "Asia"},
		{"product": "Monitor", "price": 300, "quantity": 9, "category": "Electronics", "region": "America"},
		{"product": "Keyboard", "price": 100, "quantity": 15, "category": "Electronics", "region": "Europe"},
		{"product": "Sofa", "price": 700, "quantity": 2, "category": "Furniture", "region": "Asia"},
	]

	'''
	# Read data from JSON file
	with open("sales_data.json", "r") as file:
		sales_data = json.load(file)
	'''
		
	collection.insert_many(sales_data)
	print("✅ Data inserted successfully!")

---

## 2. Find: Display all documents

	print("\n All documents:")
	for doc in collection.find():
		print(doc)
	add Codeadd Markdown

---

## 3. Query: Querying with condition

	# Products with price greater than 500
	print("\n Products with price > 500:")
	for doc in collection.find({"price": {"$gt": 500}}):
		print(doc)

	# Show only product name and price (projection)
	print("\n Only product name and price:")
	for doc in collection.find({}, {"_id": 0, "product": 1, "price": 1}):
		print(doc)

	# Electronics in Europe
	print("\n Electronics in Europe:")
	for doc in collection.find({"category": "Electronics", "region": "Europe"}):
		print(doc)
	
---
	
## 4. Sorting documents

	print("\n Sort by descending price:")
	for doc in collection.find().sort("price", -1):
		print(doc)
	
---

## 5. Count documents

	total_docs = collection.count_documents({})
	electronics_docs = collection.count_documents({"category": "Electronics"})
	print(f"\n Total documents: {total_docs}")
	print(f"Electronics products: {electronics_docs}")

---

## 6. Update documents

	# Update price of Tablet to 500
	collection.update_one({"product": "Tablet"}, {"$set": {"price": 500}})

	# Increase price of all Furniture products by 10%
	collection.update_many(
		{"category": "Furniture"},
		{"$mul": {"price": 1.1}}
	)

---

## 7. Delete documents


	# Delete product "Keyboard"
	collection.delete_one({"product": "Keyboard"})

	# Delete all products in Asia with price < 200
	collection.delete_many({"region": "Asia", "price": {"$lt": 200}})

	print("\n All documents:")
	for doc in collection.find():
		print(doc)

---

## 8. Aggregation: Aggregation Pipeline

	# Calculate total revenue, average price, and total quantity by category
	print("\n📈 Aggregation: revenue and quantity by category")
	pipeline = [
		{
			"$group": {    # ~: group by
				"_id": "$category",   # ~: grouping key      
				"total_revenue": {"$sum": {"$multiply": ["$price", "$quantity"]}},
				"average_price": {"$avg": "$price"},
				"total_quantity": {"$sum": "$quantity"}
			}
		},
		{"$sort": {"total_revenue": -1}}
	]
	agg_result = list(collection.aggregate(pipeline))
	for item in agg_result:
		print(item)


---

## 9. Create DataFrame: Convert aggregation result to Pandas DataFrame

	import pandas as pd

	df = pd.DataFrame(agg_result)
	print("\n📊 Aggregated data as DataFrame:")
	display(df)


---

## 10. Insert DataFrame into MongoDB

	df2 = pd.DataFrame({
		"region": ["Europe", "Asia", "America"],
		"year": [2023, 2023, 2023],
		"sales": [15000, 18000, 12000]
	})
	collection2 = client["datascience_db"]["region_sales"]
	collection2.drop()
	# Convert the DataFrame to a dictionary of records and insert into MongoDB
	collection2.insert_many(df2.to_dict("records"))


---

## 11. Indexing for better performance (search speed)

	collection.create_index("product")
	collection.create_index([("price", -1), ("quantity", 1)])

---

## 12. Complex queries with logical operators¶
	add Codeadd Markdown
