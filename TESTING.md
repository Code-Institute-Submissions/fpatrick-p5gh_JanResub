# Testing

- [Validation](#validation)
  * [PEP8 Validator - PyCodeStyle](#pycodestyle)
  * [HTML Checker W3C Validator - https://validator.w3.org](#html-checker-w3c-validator---https---validatorw3org)
  * [JSHint Validator - https://jshint.com](#jshint-validator---https---jshintcom)
  * [Jigsaw W3C Validator - https://jigsaw.w3.org/css-validator](#jigsaw-w3c-validator---https---jigsaww3org-css-validator)
  * [Lighthouse Report](#lighthouse-report)
- [Manual Testing](#manual-testing)
- [Bugs](#bugs)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## Validation

### PEP8 Validator - PyCodeStyle

* Ignored line too long errors for automatic migration files and setting where there are big Secret Keys.

    ![2023-01-20 10 54 20](https://user-images.githubusercontent.com/39106404/213678607-9fc3fce7-d041-4a41-94b8-d635b4d3f097.jpg)

### HTML Checker W3C Validator - https://validator.w3.org

* It was found one error introduced by embed youtube iframe, necessary to display videos on product detail. It also has a info which have no impact.

    ![Screenshot 2023-01-20 at 11 20 26](https://user-images.githubusercontent.com/39106404/213683537-f49f1651-17be-4db2-af75-5bfca8e70122.png)
    ![Screenshot 2023-01-20 at 10 14 47](https://user-images.githubusercontent.com/39106404/213680497-a0b44062-893d-4734-9c64-85a59ca04176.png)
    ![Screenshot 2023-01-20 at 10 40 46](https://user-images.githubusercontent.com/39106404/213680717-a8a44611-ff54-43a4-a053-94be3e093d13.png)
    ![Screenshot 2023-01-20 at 11 17 08](https://user-images.githubusercontent.com/39106404/213683522-021d3831-4ac8-4606-8220-6b01e5ad108e.png)
    ![Screenshot 2023-01-20 at 11 22 46](https://user-images.githubusercontent.com/39106404/213683933-4888ce65-f86d-4e00-b6e6-2f97cba6d7cd.png)



### JSHint Validator - https://jshint.com

* It was manually copied and pasted on jshint. Initially the code came only with missing semicolon warning.

    ![Screenshot 2023-01-20 at 10 44 38](https://user-images.githubusercontent.com/39106404/213680165-7f1c956b-333d-44cf-a969-01aa0d4d8f08.png)
    ![Screenshot 2023-01-20 at 10 47 51](https://user-images.githubusercontent.com/39106404/213680175-c3636e53-6ae0-4287-a749-5e966282cf24.png)

* No errors found on the quantity input script. Warnings can be ignored in this scope.

    ![Screenshot 2023-01-20 at 11 11 47](https://user-images.githubusercontent.com/39106404/213682138-6a3b5b16-065e-4417-8efd-7b6323aa731a.png)


### Jigsaw W3C Validator - https://jigsaw.w3.org/css-validator

* Custom added css has no error or warnings.

    ![Screenshot 2023-01-20 at 10 15 10](https://user-images.githubusercontent.com/39106404/213684921-a64848c6-1e2e-4114-86a4-fc09e52852d3.png)

### Lighthouse Report

![Screenshot 2023-01-20 at 11 40 20](https://user-images.githubusercontent.com/39106404/213732968-d5d87504-b6e7-4cb1-aaab-5aa998487808.png)

<br />

## Manual Testing

<br />

* All this tests was performed both on desktop and mobile. The testing was not limited to the main features listed below.

| Page Name | Action | Expected Outcome | Outcome |
| --- | --- | --- | --- |
| Products | Click all products category | List all products | Pass |
| Products | Click on a product | Identify characteristics, price, review, images | Pass |
| Account | Register account | Save my info | Pass |
| Account | Login/out | Enter or exit my account | Pass |
| Account | Receive email after register | Registration successful | Pass |
| Account | View my user profile | Can see past orders and infos | Pass |
| Products | Sort the list of available products | See products by price, review, best seller | Pass |
| Products | Sort by categories | Find products inside specific category | Pass |
| Products | Search for name (or description) | Find a specific product | Pass |
| Products | Number of available | See if what I am looking for is available | Pass |
| Cart | Add or remove items from my bag | Adjust my order before the checkout | Pass |
| Cart | See total in my bag | Show how much I will pay | Pass |
| Cart | Add more quantity | I can buy more than one easily | Pass |
| Checkout | Add payment and pay | Check out with no hassles | Pass |
| Checkout | Receive order confirmation after checkout | Bring the order details | Pass |
| Checkout | Checkout the bag | Reduce stock number of products | Pass |
| Admin | Add products | Add more products to sell | Pass |
| Admin | Edit products | I can edit image, description, price, etc | Pass |
| Admin | Remove product | Can remove items that is no longer selling | Pass |
| Products | Click on a product | Users can see and write reviews | Pass |
| Products | Add product to wishlist | Product is added in my wishlist | Pass |
| Wishlist | Remove product to wishlist | Product is removed from my wishlist | Pass |
| Testimonials | Click on testimonials | All testimonials is listed | Pass |
| Footer | Click on facebook page | Open facebook gamerhood page | Pass |
| Footer | Subscribe to newsletter | Customer is registered on mailchimp newsletter | Pass |

## Bugs

* No bugs could be found in the website to date.