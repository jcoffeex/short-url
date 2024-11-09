/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./app/templates/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [],
}

// npx tailwindcss -i ./app/static/css/input.css -o ./app/static/css/output.css --watch