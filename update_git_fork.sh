#!/bin/sh

# Para manter o fork atualizado.

git remote add upstream [Endereco do repositorio original/principal]

#verificar se esta correto
git branch
#git fetch upstream
git rebase upstream/master

git merge upstream/master

git push -f origin [Seu Branch]

