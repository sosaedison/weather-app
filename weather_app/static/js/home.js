/* The add new card button */
var add_new_card_button = document.getElementById("add-new-card-button");

/* The whole container for the add new card button */
var add_new_card_button_container = document.getElementById("add-new-card");

/* The list of weather cards */
var weather_card_list_main = document.getElementById("weather-card-list-main");

/* The max number of items a weather card list can */
const MAX_LIST_LENGTH = 5;

/* Instance of weather card manager class for basic functionality
 * of weather card related actions.
 */
card_manager = WeatherCardManager(weather_card_list_main);

/* Add and event listener to the add new card button
 * so that we can add new weather cards on click */
add_new_card_button.addEventListener("click", (event) => {
  // check against max size of list
  // add new list and card to that list as well as
  //    new card button
  // otherwise just add card and new card button as normal
  let weather_card = new_weather_card();
  weather_card_list.appendChild(weather_card);
  move_add_new_card_button(weather_card_list, add_new_card_button_container);
});

/**
 * Weather card manager class with weather functions.
 */
class WeatherCardManager {
  constructor(weather_card_list_master) {
    this.weather_card_list_master = weather_card_list_master;
  }
  new_weather_card_list() {
    let weather_card = new_weather_card();
  }
  /**
   * This function returns a full weather card.
   * @returns a weather card with the right css and child elements
   */
  new_weather_card() {
    let new_list_item = document.createElement("li");
    let new_card_container = document.createElement("div");
    let new_card_body = document.createElement("div");
    let new_card_paragraph = document.createElement("p");
    let new_remove_card_button = document.createElement("button");

    new_card_container.classList.add("card");
    new_card_container.classList.add("weather-card");
    new_card_body.classList.add("card-body");
    new_remove_card_button.classList.add("remove-card-button");

    new_remove_card_button.appendChild(remove_card_button_icon_elm());

    let text = document.createTextNode("some text");
    new_card_paragraph.appendChild(text);

    new_card_body.appendChild(new_card_paragraph);
    new_card_container.appendChild(new_remove_card_button);
    new_card_container.appendChild(new_card_body);
    new_list_item.appendChild(new_card_container);

    return new_list_item;
  }

  /**
   * Adds the new card button to the end of the given list.
   * @param {Element} card_list the list that the button should be added to
   * @param {Element} add_new_card_button the button being added to the list
   */
  move_add_new_card_button(card_list, add_new_card_button) {
    card_list.appendChild(add_new_card_button);
  }

  /**
   * Simple function for returning the 'x' icon
   * @returns a i element that links to the 'x' icon
   */
  remove_card_button_icon_elm() {
    let icon = document.createElement("i");
    icon.classList.add("fas");
    icon.classList.add("fa-times");
    return icon;
  }
}
