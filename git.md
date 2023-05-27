https://git-sky.herokuapp.com/

## Введение: Хорошо подобранное введение в основные команды git

1. Знакомство с Git Commit
```
git commit -m "First commit"
git commit -m "Second commit"
```
2. Ветвление в Git
```
git branch bugFix
git checkout bugFix
```
3. Слияния веток в Git
```
git branch bugFix
git checkout bugFix
git commit -m "First commit"
git checkout main
git commit -m "Second commit"
git merge bugFix
```
4. Введение в rebase
```
git branch bugFix
git checkout bugFix
git commit -m "First commit"
git checkout main
git commit -m "Second commit"
git checkout bugFix
git rebase main
```
## Едем дальше
Следующая порция абсолютной git-крутотенюшки. Проголодались?

1. Теряем голову, или detached HEAD
```
git checkout C4
```
2. Относительные ссылки (^)
```
git checkout bugFix^
```
3. Относительные ссылки №2
```
git checkout C1
git branch -f main C6
git branch -f bugFix bugFix~3
```
4. тмена изменений в Git
```
git reset HEAD~1
git checkout pushed
git revert HEAD
```
## Перемещаем труды туда-сюда
Не стесняйтесь менять историю

1. Введение в Cherry-pick
```
git cherry-pick C3 C4 C7
```
2. Введение в интерактивный Rebase
```
git rebase -i HEAD~4
```
## Сборная солянка
Ассорти из приёмов работы с Git, хитростей и советов

1. Выберем один коммит
```
git checkout main
git cherry-pick C4
```
2. Жонглируем коммитами
```git rebase -i main
git commit --amend -m "an updated commit message"
git rebase -i main
git branch -f main caption
```
3. Жонглируем коммитами №2
```git checkout main
git cherry-pick C2
git commit --amend -m "an updated commit message"
git cherry-pick caption
```
4. git tag
```git checkout C2
git tag v1 C2
git tag v0 C1
```
5. Git describe
```git describe main
git describe side
git describe bugFix
commit -m "Finish"
```
## Продвинутый уровень
Если ты смелый, ловкий, умелый – потренируйся тут

1. Rebase over 9000 раз
```
git rebase main bugFix
git rebase bugFix side
git rebase side another
git rebase another main
```
2. Здоровая семья, или несколько родителей
```
git branch bugWork HEAD~^2~
```
3. Спутанные ветки
```
git checkout one
git cherry-pick C4 C3 C2
git checkout two
git cherry-pick C5 C4 C3 C2
git branch -f three C2
```
## Push & Pull - удалённые репозитории в Git!
Настало время поделиться своими единичками и нулями. Время коллективного программирования

1. Введение в клонирование
```git clone
```
2. Удалённые ветки
```git commit -m "First commit"
git checkout o/main
git commit -m "Second commit"
```
3. Git fetch
```git fetch
```
4. Git pull
```git pull
```
5. Коллективная работа
```git clone
git fakeTeamwork main 2
git commit -m "My commit"
git pull
```
6. Git push
```git commit -m "First commit"
git commit -m "Second commit"
git push
```
7. Расхождение в истории
```git clone
git fakeTeamwork
git commit -m "My commit"
git pull --rebase
git push
```
8. Заблокированная ветвь main
```git reset --hard o/main
git checkout -b feature C2
git push origin feature
```

## Через origin – к звёздам. Продвинутое использование Git Remotes
Весело было быть всесильным мудрым правителем...

1. Push Мастер!
```git rebase side1 side2
git rebase side2 side3
git rebase side3 main
git pull --rebase
git push
```
2. Слияние с удалённым репозиторием
```git checkout main
git pull
git merge side1
git merge side2
git merge side3
git push
```
3. Слежка за удалённым репозиторием
```git checkout -b side o/main
git commit -m "My commit"
git pull --rebase
git push
```
4. Аргументы git push
```git push origin main
git push origin foo
```
5. Аргументы для push -- расширенная версия!
```git push origin main~1:foo
git push origin foo:main
```
6. Аргументы для fetch
```git fetch origin main~1:foo
git fetch origin foo:main
git checkout foo
git merge main
```
7. Пустой источник
```git push origin :foo
git fetch origin :bar
```
8. Аргументы для pull
```git pull origin bar:foo
git pull origin main:side```
