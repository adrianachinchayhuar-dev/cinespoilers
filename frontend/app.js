const moviesContainer = document.getElementById("moviesContainer");

async function loadMovies() {
    try {
        const response = await fetch("http://127.0.0.1:8000/api/movies/?format=json");
        const movies = await response.json();

        moviesContainer.innerHTML = "";

        movies.forEach(movie => {
            const card = document.createElement("article");
            card.classList.add("movie-card");

            const genres = movie.genres_detail || [];

            card.innerHTML = `
                <div class="movie-year">${movie.release_year}</div>
                <h3>${movie.title}</h3>
                <p>${movie.description}</p>

                <div class="genres">
                    ${
                        genres.length > 0
                            ? genres.map(genre => `<span class="genre">${genre.name}</span>`).join("")
                            : `<span class="genre">Sin género</span>`
                    }
                </div>
            `;

            moviesContainer.appendChild(card);
        });

    } catch (error) {
        moviesContainer.innerHTML = `
            <p class="loading">
                No se pudo conectar con la API. Verifica que Django esté corriendo.
            </p>
        `;
    }
}

loadMovies();