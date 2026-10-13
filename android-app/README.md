# Passat B6 EcoFuel — Android App

Android-приложение (WebView), упаковывающее офлайн-мануал по автомобилю Passat B6 EcoFuel (CDGA).

## Особенности
- Полностью автономная работа без интернета (HTML/JS вшиты внутри приложения).
- Сохранение состояния чек-листов и введенных значений (через включенный `domStorageEnabled` / `localStorage`).
- Поиск, фильтрация и подсветка результатов прямо на экране смартфона.
- Темная тема приложения в тон оригинального мануала.
- Обработка аппаратной кнопки «Назад» (навигация внутри страниц/поиска).

## Как получить готовый APK

### Вариант 1: Через GitHub Actions (Без установки чего-либо на Mac)
1. Если проект загружен на GitHub, перейдите во вкладку **Actions** в репозитории.
2. Запустите воркфлоу **Build Android APK** (кнопка *Run workflow*), либо он соберется автоматически при любом `git push`.
3. Скачайте готовый `app-debug.apk` из блока **Artifacts**.

### Вариант 2: Через Android Studio
1. Скачайте и установите бесплатную [Android Studio](https://developer.android.com/studio).
2. Выберите **File → Open** и укажите папку `android-app`.
3. Дождитесь автоматической синхронизации Gradle.
4. В верхнем меню выберите **Build → Build Bundle(s) / APK(s) → Build APK(s)**.
5. Готовый файл появится в папке: `app/build/outputs/apk/debug/app-debug.apk`.

### Вариант 3: Сборка через терминал
При наличии установленного JDK 17+ и Android SDK:
```bash
cd android-app
./gradlew assembleDebug
```
Готовый APK: `android-app/app/build/outputs/apk/debug/app-debug.apk`.
