import mysql.connector
from mysql.connector import errorcode


config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',  
    'database': 'students',
    'raise_on_warnings': True  # Activer l'affichage des avertissements MySQL
}

def create_connection():
    try:
        cnx = mysql.connector.connect(**config)
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Invalid user or password!')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database doesn't exist!")
        else:
            print('Error:', err)
        return None  # Ne pas continuer si jamais il y a une erreur de connexion
    
def recuperer_info():
    global ages
    cnx = create_connection()
    if cnx is None:
        print("Erreur de connexion")
        return []
    
    cursorSel = cnx.cursor()  # Un curseur est une structure de données qui contient des infos pour interroger la BDD
    selectAction = ("SELECT age FROM student")  # Créer une structure de tuple contenant ma requête
 

    cursorSel.execute(selectAction)  # Exécuter la requête
    resultSelect = cursorSel.fetchall()  # Récupérer les informations avec la fonction fetchall et les stocker
    ages = [col[0] for col in resultSelect]
    print(f'{ages}')
    
    cursorSel.close()  # Fermer le curseur après avoir récupéré les infos
    cnx.close()  # Fermer la connexion à la base de données
    return ages

#recuperer_info() pour tester la BDD
#Aller loin : récuperer un array age + nom (perspectives)