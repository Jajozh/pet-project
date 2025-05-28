 ### Подготовка перед запуском тестов  
1. Авторизоваться в Telegram через WEB версию
2.  Перейти в DevTools -> Console и выполнить код
```javascript
const localStorageData = JSON.stringify(localStorage, null, 2);
console.log(localStorageData);
```
Этот код преобразует содержимое localStorage в читаемый JSON-формат и выведет его в консоль - скобпировать и заменить данные в файл local_storage.json
