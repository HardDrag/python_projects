def parityEncode(data):
    # Z int do listy
    raw_data = [int(i) for i in str(data)]
    coded_data = []
    ones = 0

    # Zliczenie jedynek
    for i in raw_data:
        if i == 1:
            ones += 1
    
    # Dodanie bitu parzystości
    if ones % 2 == 1:
        coded_data = raw_data.copy()
        coded_data.append(1)
    else: 
        coded_data = raw_data.copy()
        coded_data.append(0)

    # Zwrócenie listy
    return coded_data

def parityDecode(data):
    ones = 0
    seq_valid = False

    # Zliczenie jedynek
    for i in data:
        if i == 1:
            ones += 1
    
    # Sprawdzenie bitu parzystości
    if ones % 2 == 0:
        seq_valid = True
    else: 
        seq_valid = False

    # Zwrócenie zmiennej
    return seq_valid


def compareParity(encoded, corrupted):
    corrupted_bits = []
    types_dict = {
        "parity_bit_valid": True,
        "bits_not_valid": 0,
        "bits_not_valid_pos": []
    }

    for indx, (i,j) in enumerate(zip(encoded, corrupted)):
        if i != j:
            types_dict["bits_not_valid"] += 1
            corrupted_bits.append(indx)
    
    types_dict["bits_not_valid_pos"] = corrupted_bits

    if encoded[-1] == corrupted[-1]:
        types_dict["parity_bit_valid"] = True
    else:
        types_dict["parity_bit_valid"] = False

    return types_dict


# Zakodowanie przykładowego ciągu znaków
sample_bits = 101011100101100
encoded = parityEncode(sample_bits)
print("Przed kodowaniem: ",sample_bits)
print("Po kodowaniu:     ", int(''.join(str(i) for i in encoded)))

corrupted = encoded.copy()

# Zmiana bitów do testów
# Bity mogą zostać uznane za poprawne pomimo zmiany (niedoskonałość algorytmu)
corrupted[5] = 0
corrupted[-1] = 1

print("Po zmianie bitu:  ", int(''.join(str(i) for i in corrupted)))

# Odkodowanie przykładowego ciągu znaków
seq_valid = parityDecode(corrupted)

# Informacja w zależności od wyników
if seq_valid:
    print("Dane poprawne")
else:
    print("Dane niepoprawne")

par_dict = compareParity(encoded, corrupted)

if par_dict["parity_bit_valid"]:
    print("Bit parzystości poprawny")
else:
    print("Bit parzystości niepoprawny")

print("Ilość bitów przekłamanych:   ", par_dict["bits_not_valid"])
print("Pozycje bitów przekłamanych: ", ', '.join(map(str, par_dict["bits_not_valid_pos"])))