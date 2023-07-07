from ..models.user_model import User, Address

def create_new_user(json):
    old_user_name = json.get('userName')
    print("i am inside create_new_user")
    try:
        temp_user = User.objects.get(user_name = old_user_name)
        return False
    except:
        new_user = User()
        new_user.user_name = json.get('userName')
        new_user.first_name = json.get('firstName')
        new_user.last_name = json.get('lastName')
        new_user.email = json.get('email')
        new_user.save()
        return True

def create_new_address(json):
    old_user_name = json.get('userName')
    print(old_user_name)
    try:
        print("inside try address")
        Address.objects.get(user_name = old_user_name)
        address = Address.objects.get(user_name = old_user_name)
        address.address = json.get('address')
        address.city = json.get('city')
        address.postal_code = json.get('postalCode')
        address.country = json.get('country')
        address.save()
        return False
    except:
        new_address = Address()
        new_address.user_name = json.get('userName')
        new_address.address = json.get('address')
        new_address.city = json.get('city')
        new_address.country = json.get('country')
        new_address.postal_code = json.get('postalCode')
        new_address.save()
        return True
