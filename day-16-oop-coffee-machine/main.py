from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
# print(menu.get_items())
# menu_item = menu.find_drink("latte")
# print(menu_item.cost)
# print(menu_item.ingredients)
# print(menu_item.name)

maker = CoffeeMaker()
# maker.report()
# print(maker.is_resource_sufficient(menu_item))
# maker.make_coffee(menu_item)

money = MoneyMachine()
# money.report()
# print(money.make_payment(menu_item.cost))

machine_on = True

while machine_on:

    # TODO 1: Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
    # a. Check the user’s input to decide what to do next.

    user_choice = input(f"What would you like? ({menu.get_items()}): ").lower()

    # b. The prompt should show every time action has completed, e.g. once the drink is
    # dispensed. The prompt should show again to serve the next customer.
    # the machine. Your code should end execution when this happens

    # TODO 2: Turn off the Coffee Machine by entering “ off ” to the prompt.
    # For maintainers of the coffee machine, they can use “off” as the secret word to turn off

    if user_choice == 'off':
        machine_on = False

    # TODO 3: Print report.
    # When the user enters “report” to the prompt, a report should be generated that shows
    # the current resource values.

    elif user_choice == "report":
        maker.report()
        money.report()

    # TODO 4: Check resources sufficient?
    # a. When the user chooses a drink, the program should check if there are enough
    # resources to make that drink.
    # b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
    # not continue to make the drink but print: “ Sorry there is not enough water. ”
    # c. The same should happen if another resource is depleted, e.g. milk or coffee.

    elif user_choice == 'espresso' or user_choice == 'latte' or user_choice == 'cappuccino':

        menu_item = menu.find_drink(user_choice)

        # TODO 5: Process coins.
        # a. If there are sufficient resources to make the drink selected, then the program should
        # prompt the user to insert coins.
        # b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
        # c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
        # pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
        if maker.is_resource_sufficient(menu_item):

            # TODO 6: Check transaction successful?
            # a. Check that the user has inserted enough money to purchase the drink they selected.
            # E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
            # program should say “ Sorry that's not enough money. Money refunded. ”.
            # b. But if the user has inserted enough money, then the cost of the drink gets added to the
            # machine as the profit and this will be reflected the next time “report” is triggered. E.g.
            # Water: 100ml
            # Milk: 50ml
            # Coffee: 76g
            # Money: $2.5
            # c. If the user has inserted too much money, the machine should offer change.
            # E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
            # places.
            if money.make_payment(menu_item.cost):
                # TODO 7: Make coffee
                # a. If the transaction is successful and there are enough resources to make the drink the
                # user selected, then the ingredients to make the drink should be deducted from the
                # coffee machine resources.
                # E.g. report before purchasing latte:
                # Water: 300ml
                # Milk: 200ml
                # Coffee: 100g
                # Money: $0
                # Report after purchasing latte:
                # Water: 100ml
                # Milk: 50ml
                # Coffee: 76g
                # Money: $2.5
                # b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
                # latte was their choice of drink.
                maker.make_coffee(menu_item)

