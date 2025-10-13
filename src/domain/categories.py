def categorize(description: str) -> str:
    """Categorizes an expense based on keywords in the description.

    Args:
        description (str): The description of the expense.

    Returns:
        str: The category of the expense.
    """
    desc = description.lower()
    
    # Define keyword-category mappings
    keywords = {
        "comida": "Comidas fuera de casa",
        "pizza": "Comidas fuera de casa",
        "almuerzo": "Comidas fuera de casa",
        "bebe": "Bebé",
        "pañal": "Bebé",
        "leche": "Bebé",
        "ropa": "Ropa",
        "polo": "Ropa",
        "pantalón": "Ropa",
        "regalo": "Regalos",
        "cumple": "Regalos",
        "cine": "Entretenimiento familiar",
        "netflix": "Entretenimiento familiar",
        "disney": "Entretenimiento familiar",
        "bus": "Transporte",
        "taxi": "Transporte",
        "gasolina": "Transporte",
        "agua": "Servicios básicos",
        "luz": "Servicios básicos",
        "internet": "Servicios básicos",
        "servicio": "Servicios básicos",
    }

    # Check for keywords in the description and return the corresponding category
    for keyword, category in keywords.items():
        if keyword in desc:
            return category

    return "Otros"  # Default category if no keywords match