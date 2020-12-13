import json

import pandas

data_name = []
data_stars = []
data_address = []
data_state = []
data_wi = []
data_hours = []
data_sunday = []
data_sunday_close = []
data_appointment = []
data_restaurant_price = []
data_categories = []
data_first_category = []
data_restaurant = []

with open('business_sample.json', encoding="utf8") as f:
	for line in f:
		json_line = json.loads(line)

		# To get the name of the business
		cell_name = json_line.get('name')
		data_name.append(cell_name)

		# # To get the address of the business
		cell_address = json_line.get('address')
		data_address.append(cell_address)

		# # To get the stars score
		cell_stars = json_line.get('stars')
		data_stars.append(cell_stars)

		
		# # To get the state
		cell_state = json_line.get('state')
		data_state.append(cell_state)

		# # To get a variable indicating whether the business is in Wisconsin
		cell_wi = (cell_state == "WI")
		data_wi.append(cell_state == "WI")
		
		# # To get the opening time
		cell_hours = json_line.get('hours')
		data_hours.append(cell_hours)

		# # To get the Sunday hours, and 'None' if it is not open on Sunday.
		if cell_hours is not None:
			cell_sunday = cell_hours.get('Sunday')
		else:
			cell_sunday = None
		data_sunday.append(cell_sunday)		

		# # To get closing time on Sunday, and 'None' if it is not open on Sunday.
		if cell_sunday is not None:
			cell_sunday_close = cell_sunday.split('-')[1]
		else:
			cell_sunday_close = None
		data_sunday_close.append(cell_sunday_close)	

		# # To get whether the business is by appointment only, 'None' if the business did not specified that of it does not have any attributes.
		cell_attribute = json_line.get('attributes')
		if cell_attribute is not None:
			cell_appointment = cell_attribute.get('ByAppointmentOnly')
			if cell_appointment is not None:
				data_appointment.append(cell_appointment)
			else:
				data_appointment.append(None)
		else:
			data_appointment.append(None)


		# # To get restaurant price range, 'None' if the business did not specified that of it does not have any attributes.
		if cell_attribute is not None:
			cell_restaurant_price = cell_attribute.get('RestaurantsPriceRange2')
			if cell_restaurant_price is not None:
				data_restaurant_price.append(cell_restaurant_price)
			else:
				data_restaurant_price.append(None)
		else:
			data_restaurant_price.append(None)

		# # To get all the categories
		cell_categories = json_line.get('categories')
		data_categories.append(cell_categories)

		# # To get only the first category
		if cell_categories is not None:
			cell_first_category = cell_categories.split(', ')[0]
			data_first_category.append(cell_first_category)
		else:
			data_first_category.append(None)


		# # To get a variable indicating whether 'restaurant' is one of the items in categories. 
		if cell_categories is not None:
			cell_restaurant = ('Restaurants' in cell_categories)
			data_restaurant.append(cell_restaurant)
		else:
			data_restaurant.append(None)

		
		
dataset = pandas.DataFrame(data={'name':  data_name, 
								'stars':  data_stars, 
								'address': data_address,
								'state': data_state,
								'WI': data_wi,
								'hours': data_hours,
								'sunday': data_sunday,
								'sunday_close_time': data_sunday_close,
								'by_appointment_only': data_appointment,
								'restaurant_price': data_restaurant_price,
								'categories': data_categories,
								'first_category': data_first_category,
								'restaurant': data_restaurant
								})


print(dataset)



