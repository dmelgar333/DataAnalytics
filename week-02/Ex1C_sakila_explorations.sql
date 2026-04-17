/*
a) Inside the Columns tab, actor_id, first_name, last_name, last_update.
b) In the Actor tab, actor, address, category, city, country, customer, film, film_actor, film_category, film_text, inventory, language, payment, rental, staff, store.
c) The other tables that include both are film_actor and film_category
d) This includes rental dates, return dates and ID numbers; The information is easy to read.
e) It shows inventory_id, film_id, store_id and last_update.
f) The tables I need to use in order to understand the names of all films that were rented on the specific date are rental and payment. 
*/

SELECT film_id FROM inventory_id;
SELECT rental_id FROM rental_date;
