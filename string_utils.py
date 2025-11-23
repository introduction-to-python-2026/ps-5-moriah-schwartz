def split_before_uppercases(formula):
    split_formula = []
    start = 0
    for i in range(1, len(formula)):
        if formula[i].isupper():
            split_formula.append(formula[start:i])
            start = i
    if formula:
        split_formula.append(formula[start:])
    return split_formula

def split_at_digit(formula):
    for i, char in enumerate(formula):
        if char.isdigit():
            prefix = formula[:i]
            numeric_part = int(formula[i:])
            return (prefix, numeric_part)
    return (formula, 1)

def count_atoms_in_molecule(molecular_formula):
    dict_of_atoms = {}
    split_formula = split_before_uppercases(molecular_formula)
    for atom in split_formula:
        atom_name, atom_count = split_at_digit(atom)
        dict_of_atoms[atom_name] = atom_count
    return dict_of_atoms



def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
