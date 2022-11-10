
#dictionary action

element = {
    "symbol": "AC",
    "name": "actinium",
    "mass": 227

}

print (element)

def make_periodic_table():
    periodic_table_list = [    
        {"symbol":"Ac", "name": "Actinium", "mass":	227},
        {"symbol":"Ag", "name": "Silver", "mass":	107.8682},
        {"symbol":"Al", "name": "Aluminum", "mass":	26.9815386},
        {"symbol":"Ar", "name": "Argon", "mass":	39.948},
        {"symbol":"As", "name": "Arsenic", "mass":	74.9216},
        {"symbol":"At", "name": "Astatine", "mass":	210},
        {"symbol":"Au", "name": "Gold", "mass":	196.966569},
        {"symbol":"B", "name": "Boron", "mass":	10.811},
        {"symbol":"Ba", "name": "Barium", "mass":	137.327},
        {"symbol":"Be", "name": "Beryllium", "mass":	9.012182},
        {"symbol":"Bi", "name": "Bismuth", "mass":	208.9804},
        {"symbol":"Br", "name": "Bromine", "mass":	79.904},
        {"symbol":"C", "name": "Carbon", "mass":	12.0107},
        {"symbol":"Ca", "name": "Calcium", "mass":	40.078},
        {"symbol":"Cd", "name": "Cadmium", "mass":	112.411},
        {"symbol":"Ce", "name": "Cerium", "mass":	140.116},
        {"symbol":"Cl", "name": "Chlorine", "mass":	35.453},
        {"symbol":"Co", "name": "Cobalt", "mass":	58.933195},
        {"symbol":"Cr", "name": "Chromium", "mass":	51.9961},
        {"symbol":"Cs", "name": "Cesium", "mass":	132.9054519},
        {"symbol":"Cu", "name": "Copper", "mass":	63.546},
        {"symbol":"Dy", "name": "Dysprosium", "mass":	162.5},
        {"symbol":"Er", "name": "Erbium", "mass":	167.259},
        {"symbol":"Eu", "name": "Europium", "mass":	151.964},
        {"symbol":"F", "name": "Fluorine", "mass":	18.9984032},
        {"symbol":"Fe", "name": "Iron", "mass":	55.845},
        {"symbol":"Fr", "name": "Francium", "mass":	223},
        {"symbol":"Ga", "name": "Gallium", "mass":	69.723},
        {"symbol":"Gd", "name": "Gadolinium", "mass":	157.25},
        {"symbol":"Ge", "name": "Germanium", "mass":	72.64},
        {"symbol":"H", "name": "Hydrogen", "mass":	1.00794},
        {"symbol":"He", "name": "Helium", "mass":	4.002602},
        {"symbol":"Hf", "name": "Hafnium", "mass":	178.49},
        {"symbol":"Hg", "name": "Mercury", "mass":	200.59},
        {"symbol":"Ho", "name": "Holmium", "mass":	164.93032},
        {"symbol":"I", "name": "Iodine", "mass":	126.90447},
        {"symbol":"In", "name": "Indium", "mass":	114.818},
        {"symbol":"Ir", "name": "Iridium", "mass":	192.217},
        {"symbol":"K", "name": "Potassium", "mass":	39.0983},
        {"symbol":"Kr", "name": "Krypton", "mass":	83.798},
        {"symbol":"La", "name": "Lanthanum", "mass":	138.90547},
        {"symbol":"Li", "name": "Lithium", "mass":	6.941},
        {"symbol":"Lu", "name": "Lutetium", "mass":	174.9668},
        {"symbol":"Mg", "name": "Magnesium", "mass":	24.305},
        {"symbol":"Mn", "name": "Manganese", "mass":	54.938045},
        {"symbol":"Mo", "name": "Molybdenum", "mass":	95.96},
        {"symbol":"N", "name": "Nitrogen", "mass":	14.0067},
        {"symbol":"Na", "name": "Sodium", "mass":	22.98976928},
        {"symbol":"Nb", "name": "Niobium", "mass":	92.90638},
        {"symbol":"Nd", "name": "Neodymium", "mass":	144.242},
        {"symbol":"Ne", "name": "Neon", "mass":	20.1797},
        {"symbol":"Ni", "name": "Nickel", "mass":	58.6934},
        {"symbol":"Np", "name": "Neptunium", "mass":	237},
        {"symbol":"O", "name": "Oxygen", "mass":	15.9994},
        {"symbol":"Os", "name": "Osmium", "mass":	190.23},
        {"symbol":"P", "name": "Phosphorus", "mass":	30.973762},
        {"symbol":"Pa", "name": "Protactinium", "mass":	231.03588},
        {"symbol":"Pb", "name": "Lead", "mass":	207.2},
        {"symbol":"Pd", "name": "Palladium", "mass":	106.42},
        {"symbol":"Pm", "name": "Promethium", "mass":	145},
        {"symbol":"Po", "name": "Polonium", "mass":	209},
        {"symbol":"Pr", "name": "Praseodymium", "mass":	140.90765},
        {"symbol":"Pt", "name": "Platinum", "mass":	195.084},
        {"symbol":"Pu", "name": "Plutonium", "mass":	244},
        {"symbol":"Ra", "name": "Radium", "mass":	226},
        {"symbol":"Rb", "name": "Rubidium", "mass":	85.4678},
        {"symbol":"Re", "name": "Rhenium", "mass":	186.207},
        {"symbol":"Rh", "name": "Rhodium", "mass":	102.9055},
        {"symbol":"Rn", "name": "Radon", "mass":	222},
        {"symbol":"Ru", "name": "Ruthenium", "mass":	101.07},
        {"symbol":"S", "name": "Sulfur", "mass":	32.065},
        {"symbol":"Sb", "name": "Antimony", "mass":	121.76},
        {"symbol":"Sc", "name": "Scandium", "mass":	44.955912},
        {"symbol":"Se", "name": "Selenium", "mass":	78.96},
        {"symbol":"Si", "name": "Silicon", "mass":	28.0855},
        {"symbol":"Sm", "name": "Samarium", "mass":	150.36},
        {"symbol":"Sn", "name": "Tin", "mass":	118.71},
        {"symbol":"Sr", "name": "Strontium", "mass":	87.62},
        {"symbol":"Ta", "name": "Tantalum", "mass":	180.94788},
        {"symbol":"Tb", "name": "Terbium", "mass":	158.92535},
        {"symbol":"Tc", "name": "Technetium", "mass":	98},
        {"symbol":"Te", "name": "Tellurium", "mass":	127.6},
        {"symbol":"Th", "name": "Thorium", "mass":	232.03806},
        {"symbol":"Ti", "name": "Titanium", "mass":	47.867},
        {"symbol":"Tl", "name": "Thallium", "mass":	204.3833},
        {"symbol":"Tm", "name": "Thulium", "mass":	168.93421},
        {"symbol":"U", "name": "Uranium", "mass":	238.02891},
        {"symbol":"V", "name": "Vanadium", "mass":	50.9415},
        {"symbol":"W", "name": "Tungsten", "mass":	183.84},
        {"symbol":"Xe", "name": "Xenon", "mass":	131.293},
        {"symbol":"Y", "name": "Yttrium", "mass":	88.90585},
        {"symbol":"Yb", "name": "Ytterbium", "mass": 173.054},
        {"symbol":"Zn", "name": "Zinc", "mass":	65.38},
        {"symbol":"Zr", "name": "Zirconium", "mass": 91.22},
    ]
    return periodic_table_list
class FormulaError(ValueError):
    """FormulaError is the type of error that the parse_formula
    function will raise if a formula is invalid.
    """


def parse_formula(formula, periodic_table_dict):
    """Convert a chemical formula for a molecule into a compound
    list that stores the quantity of atoms of each element
    in the molecule. For example, this function will convert
    "H2O" to [["H", 2], ["O", 1]] and
    "PO4H2(CH2)12CH3" to [["P", 1], ["O", 4], ["H", 29], ["C", 13]]

    Parameters
        formula is a string that contains a chemical formula
        periodic_table_dict is the compound dictionary returned
            from make_periodic_table
    Return: a compound list that contains chemical symbols and
        quantities like this [["Fe", 2], ["O", 3]]
    """
    assert isinstance(formula, str), \
        "wrong data type for parameter formula; " \
        f"formula is a {type(formula)} but must be a string"
    assert isinstance(periodic_table_dict, dict), \
        "wrong data type for parameter periodic_table_dict; " \
        f"periodic_table_dict is a {type(periodic_table_dict)} " \
        "but must be a dictionary"

    def parse_quant(formula, index):
        quant = 1
        if index < len(formula) and formula[index].isdecimal():
            start = index
            index += 1
            while index<len(formula) and formula[index].isdecimal():
                index += 1
            quant = int(formula[start:index])
        return quant, index

    def get_quant(elem_dict, symbol):
        return 0 if symbol not in elem_dict else elem_dict[symbol]

    def parse_r(formula, index, level):
        start_index = index
        start_level = level
        elem_dict = {}
        while index < len(formula):
            ch = formula[index]
            if ch == "(":
                group_dict, index = parse_r(formula,index+1,level+1)
                quant, index = parse_quant(formula, index)
                for symbol in group_dict:
                    prev = get_quant(elem_dict, symbol)
                    curr = prev + group_dict[symbol] * quant
                    elem_dict[symbol] = curr
            elif ch.isalpha():
                symbol = formula[index:index+2]
                if symbol in periodic_table_dict:
                    index += 2
                else:
                    symbol = formula[index:index+1]
                    if symbol in periodic_table_dict:
                        index += 1
                    else:
                        raise FormulaError("invalid formula, "
                            f"unknown element symbol: {symbol}",
                            formula, index)
                quant, index = parse_quant(formula, index)
                prev = get_quant(elem_dict, symbol)
                elem_dict[symbol] = prev + quant
            elif ch == ")":
                if level == 0:
                    raise FormulaError("invalid formula, "
                        "unmatched close parenthesis",
                        formula, index)
                level -= 1
                index += 1
                break
            else:
                if ch.isdecimal():
                    # Decimal digit not preceded by an
                    # element symbol or close parenthesis
                    message = "invalid formula"
                else:
                    # Illegal character: [^()0-9a-zA-Z]
                    message = "invalid formula, illegal character"
                raise FormulaError(message, formula, index)
        if level > 0 and level >= start_level:
            raise FormulaError("invalid formula, "
                "unmatched open parenthesis",
                formula, start_index - 1)
        return elem_dict, index

    # Return the compound list of element symbols and
    # quantities. Each element in the compound list
    # will be a list in this form: ["symbol", quantity]
    elem_dict, _ = parse_r(formula, 0, 0)
    return list(elem_dict.items())


# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1

# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1


def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the
    elements listed in symbol_quantity_list.

    Parameters
        symbol_quantity_list is a compound list returned
            from the parse_formula function. Each small
            list in symbol_quantity_list has this form:
            ["symbol", quantity].
        periodic_table_dict is the compound dictionary
            returned from make_periodic_table.
    Return: the total molar mass of all the elements in
        symbol_quantity_list.

    For example, if symbol_quantity_list is [["H", 2], ["O", 1]],
    this function will calculate and return
    atomic_mass("H") * 2 + atomic_mass("O") * 1
    1.00794 * 2 + 15.9994 * 1
    18.01528
    """
    # Do the following for each each inner list in the
    for list in symbol_quantity_list:
        symbol = list[1]
        print(symbol)
        # Multiply the atomic mass by the quantity.
        # Add the product into the total molar mass.

    # Return the total molar mass.
    return






def main():
    # Get a chemical formula for a molecule from the user.
    chemical_formula = input("what is the chemical formula for the molecule: ")
    # Get the mass of a chemical sample in grams from the user.
    gram_mass = input("What is the mass in grams: ")
    # Call the make_periodic_table function and
    # store the periodic table in a variable.
    elements = make_periodic_table()
    # Call the parse_formula function to convert the
    # chemical formula given by the user to a compound
    # list that stores element symbols and the quantity
    # of atoms of each element in the molecule.
    parse_formula(chemical_formula, element)
    # Call the compute_molar_mass function to compute the
    # molar mass of the molecule from the compound list.

    # Compute the number of moles in the sample.

    # Print the molar mass.

    # Print the number of moles.

    
   

if __name__ == "__main__":
    main()