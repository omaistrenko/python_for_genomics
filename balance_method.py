#BALANCED METHOD
 
#norm - norm of active substance - this is the return value of formula;
# harvest_planned - planed harvest, kg/hectare;
# nutr_removal - nutrient removal,kg;
# nutr_stock_soil - stock of nutrients in soil, hundredweight/hectare;

# a - coeficient of nutrient utilization;
# organic_norm1 and organic_norm2 - norm of organic fertilizers, tons/hectare;
# nutr_content_org - content of nutrients in 1 ton of organic fertilizers;
# b1 and b2 coeficients of substance utilization from organic fertilizers in first and second year respectevely;
# nutr_inorg - quantity of nutrients introduced previously, kg/hectare;
# y1 and y2 coeficients of nutrients utilization from mineral fertilizers in first and second year respectevely;

def balance_method(harvest_planned, nutr_removal, nutr_stock_soil, a, organic_norm1, organic_norm2, nutr_content_org, b1, b2, nutr_inorg, y1, y2):
	return (100*harvest_planned*nutr_removal - nutr_stock_soil*a - organic_norm2*nutr_content_org*b2 - nutr_inorg*y2 - organic_norm1*nutr_content_org*b1)/y1
	
def test_balance_method(harvest_planned, nutr_removal, nutr_stock_soil, a, organic_norm1, organic_norm2, nutr_content_org, b1, b2, nutr_inorg, y1, y2):
	print str(balance_method(harvest_planned, nutr_removal, nutr_stock_soil, a, organic_norm1, organic_norm2, nutr_content_org, b1, b2, nutr_inorg, y1, y2))
	
test_balance_method(1,1,1,1,1,1,1,1,1,1,1,1)

#BALANCED_CALCULATION METHOD
#this is a simplified version of balanced method
#
def balanced_calc_method(harvest_planned, nutr_removal, nutr_stock_soil, a, organic_norm1, nutr_content_org, b1, y1):
	return (100*harvest_planned*nutr_removal - nutr_stock_soil*a - organic_norm1*nutr_content_org*b1)/y1

def test_balanced_calc_method(harvest_planned, nutr_removal, nutr_stock_soil, a, organic_norm1, nutr_content_org, b1, y1):
	print str(balanced_calc_method(harvest_planned, nutr_removal, nutr_stock_soil, a, organic_norm1, nutr_content_org, b1, y1))
	
test_balanced_calc_method(1,1,1,1,1,1,1,1)