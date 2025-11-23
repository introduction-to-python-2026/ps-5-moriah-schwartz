def split_by_capitals(formula):
    if not formula:
      return[]
    start = 0
    end = 1
    split_formula = []

    for char in formula[1:]:
        if char.isupper():               
            split_formula.append(formula[start:end])
            start = end                 
        end += 1                        

    split_formula.append(formula[start:end])

    return split_formula


def split_at_number(formula):
    digit_location = 1

    for char in formula[1:]:
        if char.isdigit():
            break
        digit_location += 1

    if digit_location == len(formula):
        return formula, 1

    prefix = formula[:digit_location]
    number_part = formula[digit_location:]

    return prefix, int(number_part)

def count_atoms_in_molecule(molecular_formula):
    dict_of_atoms = {}
    split_formula = split_by_capitals(molecular_formula)
    for atom in split_formula:
        atom_name, atom_count = split_at_number(atom)
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
