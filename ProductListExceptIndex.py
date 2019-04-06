

def get_products_of_all_ints_except_at_index(int_list):

    
    product = 1
    product_list = []
    
    if len(int_list) < 2:
        raise ValueError("Size Less than specified")
    
    for i in range(0, len(int_list)):
        product_list.append(product)
        product = product * int_list[i]
        
    
    product = 1
    for i in range(len(int_list)-1, -1, -1):
        product_list[i] = product_list[i] * product
        product = product * int_list[i]
        
    return product_list    
   



