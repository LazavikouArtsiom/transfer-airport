form = document.getElementById('contactForm')
csrf = Array.from(document.getElementsByName('csrfmiddlewaretoken'))[0].value

form.innerHTML = `
<input type="hidden" name="csrfmiddlewaretoken" value="${csrf}">
<div class="row jc-sa">
<div class="column jc-sb">
    <div class="row-el column">
        <label for="id_name">Ваше имя</label> <input type="text" name="name" maxlength="255" required=""
            id="id_name">
    </div>
    <div class="row-el column">
        <label for="id_phone">Номер телефона</label> <input type="text" name="phone" maxlength="20"
            required="" id="id_phone">

    </div>
    <div class="row-el column">
        <label for="id_email">Email:</label> <input type="text" name="email" maxlength="30" required=""
            id="id_email">

    </div>
</div>
<div class="column jc-sb">
    <div class="row-el column">
        <label for="id_city">Город</label> <select name="city" id="id_city">
            <option value="1" selected="">Могилёв</option>

            <option value="2">Шклов</option>

            <option value="3">Бобруйск</option>

            <option value="4">Гомель</option>

            <option value="5">Орша</option>

        </select>
    </div>
    <div class="row-el column">
        <label for="id_airport">Аэропорт:</label>
        <select name="airport" id="id_airport">
        <option value="1" selected="">а/п Борисполь</option>
      
        <option value="2">а/п Шереметьево</option>
      
        <option value="3">а/п Внуково</option>
      
        <option value="4">а/п Домодедово</option>
      
        <option value="5">а/п Остафьево</option>
      
        <option value="6">а/п Жуковский</option>
      
      </select>
    </div>
    <div class="row-el column">
        <p class="column"><label for="id_count">Количество мест</label> <input type="number"
                name="count" value="1" min="0" required="" id="id_count"></p>
    </div>
</div>
<div class="column jc-sb">
    <div class="row-el column">
        <label for="id_order_date">Дата билета</label> <input type="date" name="order_date" required=""
            id="id_order_date">
    </div>
    <div class="row-el column">
        <label for="id_is_back">Обратный трансфер:</label> <input type="checkbox" name="is_back"
            id="id_is_back" checked="">
    </div>
    <div class="row-el column">
        <label for="id_back_date">Дата возвращения:</label> <input type="date" name="back_date"
            required="" id="id_back_date">

    </div>
</div>
</div>
<div class="box column ai-c">
<label for="id_notes">Примечания</label> <textarea name="notes" cols="40" rows="10" maxlength="255"
    required="" id="id_notes"
    placeholder="кол-во детей и сколько им лет или другая информация"></textarea>
<input name="submit" id="submit" class="form-btn"
    value="Бронировать" type="submit">
</div>
`