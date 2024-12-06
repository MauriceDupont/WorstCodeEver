Documentation de AnagrammeParTriCrépusculaire

Nous avons essayé d'utiliser ChatGPT pour générer la documentation du code. Malheureusement, le code était trop étrange pour lui, voici sa réponse :

"It seems like I can’t do more advanced data analysis right now. Please try again later."

Bref, commençons la documentation du monstre. Il sert à vérifier si deux phrases sont des anagrammes, une tâche qui semble toute simple, vous diriez-vous ? CEPENDANT, malgré notre intellect supérieur à la moyenne, nous nous retrouvons avec un algorithme bien complexe. Essayons ensemble de comprendre ce qu'il fait et pourquoi il le fait.

Fonction 1 : ConvertisseurEtape1

Cette fonction convertit une phrase en une liste contenant les lettres de cette phrase, en enlevant les espaces et en transformant les majuscules en minuscules.

Fonction 2 : ConvertisseurEtape2

Elle transforme chaque lettre de la liste créée précédemment en son numéro de caractère ASCII.

Fonction 3 : ConvertisseurEtape3

Cette fonction transforme chaque numéro de la liste en son équivalent binaire.

CEPENDANT, vient le plus grand mystère de ce code : La fonction binaire convertit mal les chiffres qu'on lui donne, et nous ne savons pas pourquoi. Cela est dû à une pause trop prolongée et à l'absence de documentation. Nous avons oublié comment fonctionnait notre convertisseur binaire. Mais nous avons décidé d'ignorer l'erreur en nous disant : "Hassoul, ça passe."

Fonction 5 : EnleverZoro

Cette fonction enlève les zéros inutiles des nombres binaires (ex. : 00110 → 110).

La Grande Star du Code : Le Tri Crépusculaire

Voici un tri révolutionnaire par son inefficacité : le tri crépusculaire (car il prend toute la nuit à s'exécuter si votre liste est plus grande que la saga Harry Potter).

Fonction 6 : TriCrépusculaireEtapeUno

Cette fonction trie la liste de nombres binaires en une liste de listes, regroupant les nombres binaires de même longueur afin de faciliter leur tri.

Fonction 7 : TriCrépusculaireEtapeIchBin

Elle trie les listes présentes dans la grande liste (ex. : [[1,0],[11,10]] → [[0,1],[10,11]]).

Fonction 8 : Reassamblage

Cette fonction réduit la liste de listes en une seule liste (ex. : [[0,1],[10,11]] → [0,1,10,11]).

Fonction 9 : Tablointodec

Elle convertit les nombres binaires de la liste en nombres décimaux.

Fonction 10 : Tablodectochr

Cette fonction convertit les nombres décimaux en lettres.

Fonction 11 : ComparerListes

Elle compare les deux listes créées à l'aide de toutes les fonctions ci-dessus à partir des deux chaînes de caractères passées en entrée.

En résumé :

L'algorithme prend deux phrases en entrée, les convertit en listes de lettres, puis en chiffres, puis en binaire. Il trie les nombres binaires par ordre croissant (ce qui équivaut à trier les lettres des phrases par ordre alphabétique), réalise les conversions inverses pour revenir à des listes de lettres, et compare les deux listes. Si elles sont égales, les phrases sont des anagrammes. Sinon, elles ne le sont pas.

