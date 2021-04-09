def rotate(list_for_changing):
  """
  The function changes the list "in place": the last element of the list moves to the beginning of the list
  """
  if list_for_changing == []:
    return list_for_changing
  list_for_changing.insert(0, list_for_changing.pop(-1))
