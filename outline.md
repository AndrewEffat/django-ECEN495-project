Item:
    - title/name*
    - category
    - discription*
    - images*
    - price*
    - quantity*
    - in stock*
    - author*
    - rating/review
    - comments
    - deliveryDuration
    - AI Generated Recommendations --> "You may also like"

    - add to cart (Order)
    - buy it now (Order)

Category:
    - title
    - 


------------------------------------------------------------------


Item:
    - itemName
    - description
    - barcode/id
    - price
    - photo
    - reorder
    - inStock

Category:
    - categoryName
    + purchaseItem()
    + addItem()
    + removeItem()
    + editItem()
    + reorder()
    + email()