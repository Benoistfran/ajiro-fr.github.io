---
date: 2018-03-19
title: "Différentes manières de gérer les exceptions"
lang: fr
draft: true
authors:
  - benoist_alexis
tags:
  - Craft
categories:
  - craft
description: |
  Quelles sont les différentes façons de gérer les exceptions ?
  Voyons ce que la manière dont les différents langages procèdent.
---


<!-- https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_gestion_d%27exceptions -->

Tout programme en exécution peut être sujet à des erreurs pour lesquelles des
stratégies de détection et de réparation sont possibles. Ces erreurs ne sont
pas des bugs mais des conditions particulières (ou conditions exceptionnelles,
ou exceptions) dans le déroulement normal d'une partie d'un programme.

Prenons l'exemple du scoring de bowling. Si les entrées n'ont pas le bon format,
on doit rejeter ces entrées.

# Lever une exception avec contrat

Une méthode pout faire ça est de lever une exception. Beaucoup de langage
utilisent cette approche.

+ clair
- Problèmes d'encapsulation

```
class Mere:
  throws NotFound, UserStorageGeneralError

class Memoire:
  throws NotFound

class FileSystem:
  throws NotFound, UserStorageGeneralError avec CorruptedFile

class DB:
  throws NotFound, UserStorageGeneralError avec ConnectionError
```

```java
public class Bowling {

    public static int compute(int[] rolls) {
        checkRolls(rolls)
        return computeInner(rolls);
    }
    public static void checkRolls(int[] rolls) throws TooManyRolls, NotEnoughRolls {
        if (rolls.length > 24) throw new TooManyRolls();
        if (rolls.length < 20) throw new NotEnoughRolls();
    }

    protected static class TooManyRolls extends Throwable {
    }

    protected static class NotEnoughRolls extends Throwable {
    }
}
```

L'erreur peut être attrapée dans un bloc try/catch ou laisser planter le programme.
Plus propre de la rattraper.
La stacktrace permet de savoir d'ou vient l'erreur.
# Lever une exception sans contrat

- pas clair

# Rejeter une promesse

C'est ce qu'on fait en javascript car c'est un langage asynchrone.

Une promesse c'est un object qui promet une valeur de retour et
lorsqu'elle a fini son travail, elle peut le retourner en utilisant
la méthode resolve. Par contre s'il a une erreur dans le traitement
la promesse est rejetée.

Le constructeur de cet objet utilise une fonction avec deux arguments, un pour
résoudre la promesse et l'autre pour la rejeter.

Notre exemple est complétement synchrone, donc cela n'a pas de sens
d'utiliser une promesse, mais faisons le pour l'exemple.

```js
class TooManyRolls extends Error {
}

class NotEnoughRolls extends Error {
}

const checkRolls = function (rolls) {
  return new Promise(function (resolve, reject) {
    if (rolls.length > 24) reject(new TooManyRolls());
    if (rolls.length < 20) reject(new NotEnoughRolls());
    resolve()
  });
};
```

Il existe une autre syntaxe plus légère dans les versions récentes de
javascript. Dans la version ci-dessous le `async` devant la fonction
transforme le `throw` en reject et le return en `resolve`.

```js
const checkRolls = async (rolls) => {
  if (rolls.length > 24) throw new TooManyRolls();
  if (rolls.length < 20) throw new NotEnoughRolls();
};
```

# Retourner une valeur et une erreur dans un tuple

C'est ce que le fait go:

- notation assez lourde qui oblige à mettre des if partout dans le code.
+ explicite quand il n'y a pas d'erreur possible, on le sait

```go
package main
import "errors"
import "fmt"

func compute(rolls []int) (int, error) {
    err = checkRolls()
    if err {
        return -1, err
    }

    return computeInner(rools)
}
```
# Retourner une valeur ou une erreur dans une monade Maybe

C'est ce qu'on fait dans les langages fonctionnels comme Haskell.

Le type permet de gérer l'erreur de manière très simple.

# Retourner null

> LUKE: Le côté obscur est le plus fort.

> YODA: Non, non, non plus rapide, plus facile, plus séduisant.

> LUKE: Mais comment reconnaître le bon côté du mauvais ?

C'est facile mais c'est une mauvaise méthode car elle viole le principe de
substitution de Liskov.

# Logger

Dans sentry ou dans un fichier texte.

# Retourner un code d'erreur

C'est ce que fait le shell. Lorsque un executable ou un built-in ne
fonctionne pas, il retourne un code d'erreur différent de zéro.

+ Très perf
- Pas très lisible, on est obligé de connaitre les codes d'erreur.

# Arrêter le programme

Si on est assez haut dans le programme. C'est la bonne chose à faire.

Deux cas, utilitaire one shot vs serveur.

exception => exit => status-code

<!-- http://learnyousomeerlang.com/introduction#what-is-erlang -->
We'll see how to use most of these tools and achieve safety later on, but for now, I'll tell you about a related general policy in Erlang: Let it crash. Not like a plane with dozens of passengers dying, but more like a tightrope walker with a safety net under him. While you should avoid making mistakes, you won't need to check for every type or error condition in most cases.

Erlang's ability to recover from errors, organize code with actors and making it scale with distribution and concurrency all sound awesome, which brings us to the next section...

<!-- http://learnyousomeerlang.com/errors-and-exceptions -->
There are three kinds of exceptions in Erlang: errors, throws and exits. They all have different uses (kind of):

# Conclusion
Quel est le meilleur?
Dans quel cas, quel système est plus adapté.
