class Expense:
    """Represents an expense entry with its attributes and methods for validation and formatting."""

    def __init__(self, date: str, description: str, category: str, amount: str):
        """
        Initializes an Expense instance.

        Args:
            date (str): The date of the expense in 'dd/mm/yyyy' format.
            description (str): A brief description of the expense.
            category (str): The category of the expense.
            amount (str): The amount of the expense in 'x,yy' format.
        """
        self.date = date
        self.description = description
        self.category = category
        self.amount = amount

    def validate(self) -> bool:
        """
        Validates the expense attributes.

        Returns:
            bool: True if all attributes are valid, False otherwise.
        """
        return self._validate_date() and self._validate_amount()

    def _validate_date(self) -> bool:
        """Validates the date format."""
        try:
            day, month, year = map(int, self.date.split('/'))
            datetime.datetime(year, month, day)  # Will raise ValueError if invalid
            return True
        except ValueError:
            return False

    def _validate_amount(self) -> bool:
        """Validates the amount format."""
        try:
            amount_value = float(self.amount.replace(',', '.'))
            return amount_value >= 0  # Amount should be non-negative
        except ValueError:
            return False

    def format_expense(self) -> str:
        """
        Formats the expense details for display.

        Returns:
            str: A formatted string representation of the expense.
        """
        return f"{self.date} | {self.description} | {self.category} | {self.amount}"