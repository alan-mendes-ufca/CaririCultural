# Cariri Cultural

Aplicativo Android de turismo e cultura da região do Cariri (CE).

A documentação do projeto (requisitos, modelagem, protótipo e decisões) está na [Wiki](https://github.com/alan-mendes-ufca/CaririCultural/wiki). O planejamento está nas [issues](https://github.com/alan-mendes-ufca/CaririCultural/issues) e nos [milestones](https://github.com/alan-mendes-ufca/CaririCultural/milestones).

> [!NOTE]
> Este README cobre só a compilação do aplicativo. A visão do projeto, a stack e as regras de contribuição entram com a issue #3.

## Como compilar

### Pré-requisitos

- JDK 17 ou superior.
- Android SDK com a plataforma indicada em `compileSdk` (`app/build.gradle.kts`). O Android Studio instala o SDK. Sem ele, crie um `local.properties` na raiz com `sdk.dir=/caminho/para/o/Android/Sdk` ou defina a variável `ANDROID_HOME`.

O Gradle não precisa ser instalado: o wrapper (`./gradlew`) baixa a versão fixada em `gradle/wrapper/gradle-wrapper.properties`.

### Comandos

```bash
# Gera o APK debug em app/build/outputs/apk/debug/app-debug.apk
./gradlew assembleDebug

# Instala o APK debug no emulador ou dispositivo conectado (Android 8.0+)
./gradlew installDebug
```

No Windows, use `gradlew.bat` no lugar de `./gradlew`.

O build `release` ainda não é assinado; a assinatura e a distribuição são tratadas na issue #5.
