def is_eligible_for_discount(age, has_membership):
  """Checks if a customer qualifies for a discount based on age and membership."""
  if age >= 65 or has_membership:
    return True  # Eligible
  else:
    return False  # Not Eligible
  #prompt user for age 
  customer_age = int(input("tafadhali weka miaka yako"))


# Example usage
customer_age = 70
customer_has_membership = True

if is_eligible_for_discount(customer_age, customer_has_membership):
  print("Congratulations! You qualify for a discount.")
else:
  print("You are not eligible for a discount at this time.")