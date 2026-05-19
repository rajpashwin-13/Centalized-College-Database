document.addEventListener("DOMContentLoaded", function () {

    // Student Search

    const searchBoxes = document.querySelectorAll(".search-box");

    searchBoxes.forEach(searchBox => {

        searchBox.addEventListener("keyup", function () {

            let filter = searchBox.value.toLowerCase();

            let table =
                searchBox.closest(".card")
                         .querySelector("table");

            let rows = table.querySelectorAll("tbody tr");

            rows.forEach(row => {

                let text = row.innerText.toLowerCase();

                if (text.includes(filter)) {

                    row.style.display = "";

                } else {

                    row.style.display = "none";

                }

            });

        });

    });

});