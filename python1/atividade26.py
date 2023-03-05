#Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros, verifica se 
#tal lista possui elementos repetidos e os remove. A função deve devolver uma lista correspondente à 
#primeira lista, sem elementos repetidos. A lista devolvida deve estar ordenada.
lista = [2,2,2,3,2,1,5,6,4]
def remove_repetidos(lista):
    """Remove elementos repetidos da lista e a retorna ordenada."""
    lista_sem_repeticao = sorted(list(set(lista)))
    return lista_sem_repeticao

print(remove_repetidos(lista))