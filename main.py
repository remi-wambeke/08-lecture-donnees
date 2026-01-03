#### Imports et définition des variables globales

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    with open(filename, mode = 'r', encoding='utf8') as f:
        lines = f.readlines()
        for line in lines:
            cleaned_line = line.strip()
            elements = cleaned_line.split(';')
            int_list = [int(i) for i in elements]
            l.append(int_list)
    return l

def get_list_k(data, k):
    return data[k]

def get_first(l):
    return None

def get_last(l):
    return None

def get_max(l):
    return None

def get_min(l):
    return None

def get_sum(l):
    return None


#### Fonction principale


def main():
    pass
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
