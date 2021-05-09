#need to import the libraries I will use 
import pandas as pd

#this information would be collected from the user in the web form
#right now just have sample values

#electricity used in kWh
elec = 600
#car fuel kilometres travelled
km = 340
#heating oil purchased (in gallons) or natural gas purchased (in m3)
oil = 5
natgas = 0

#food items would be collected by the web form and turned into a table
#here I have a sample table as the intro to this code, but the table would haev been collected separately 
food = {'Food Item':  ['Milk', 'Cereal', 'Fruit', 'Cheese', 'Eggs'],
        'Weight in Grams': [1000, 600, 1100, 700, 880]
        }

food_df = pd.DataFrame (food, columns = ['Food Item','Weight in Grams'])

#here is the df of all the food LCA data we have, in the future we would connect to a database but for now this is how we have it set up
#emissions factors are in kg Co2e/kg food
#they are based on the mean found in 'Systematic review of greenhouse gas emissions for different fresh food categories' by Clune et al. pubished in Journal of Cleaner Production

#when connected to a database would use many more specific food items as well (data exists for almost every type of food), but to show example have kept it simple here

food_factors = [['Vegetable', 0.47],['Fruit', 0.5],['Cereal',0.53],['Legume', 0.66], ['Tree nut', 1.42],['Milk', 1.39],['Rice', 2.66], ['Eggs', 3.39],['Fish', 4.41],
                ['Chicken', 4.12], ['Cream', 5.32],['Pork', 5.85], ['Cheese', 8.86], ['Butter', 11.52],['Lamb', 27.91], ['Beef', 28.73]
                ]
food_factors_df = pd.DataFrame(food_factors, columns = ['Food Item', 'Emissions Factor in kg Co2e per kg food'])
food_factors_df = food_factors_df.set_index('Food Item')

#here are the emissions factors for electricity, oil, natural gas, and vehicle km
elec_emission_factor = 201  #this is in t Co2e/Gwh
heating_oil_emission_factor = 10.18409 #this is in kg Co2e per gallon of heating oil
heating_natural_gas_emission_factor = 54.49555 #this is in g Co2e per scf of natural gas
car_emissions_factor = 404 #in grams per mile 

#calculate emissions for each electricity, oil and vehicle km
elec_emissions = (elec_emission_factor * 1016.04691) * (elec / 1000000) #includes unit conversions to end up with kg co2e
heating_emissions = (heating_oil_emission_factor*oil) + ((heating_natural_gas_emission_factor*natgas*35.3146667)/1000) #includes unit conversions to end up with kg co2e
car_emissions = (car_emissions_factor*km*0.62137119)/1000 #includes unit conversions to end up with kg co2e

#then to calculate the food emissions
#set food emissions 
food_emissions = 0
ticker = 0

#for each item in list add up the emissions 
for i in food_df['Food Item']: 
  food_emissions = food_emissions + (food_factors_df['Emissions Factor in kg Co2e per kg food'][i]*((food_df['Weight in Grams'][ticker])/1000))
  ticker = ticker +1 

#outputs 

print('Electricity Emissions are: ' + str(round(elec_emissions)) + ' kg co2e')
print('Heating Emissions are: ' + str(round(heating_emissions)) + ' kg co2e')
print('Driving Emissions are: ' + str(round(car_emissions)) + ' kg co2e')
print('Food Emissions are: ' + str(round(food_emissions)) + ' kg co2e')

#emissions factors from journal articles, ontario government, and the EPA
