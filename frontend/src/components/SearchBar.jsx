function SearchBar({ searchTerm, setSearchTerm }) {
  return (
    <input
      type="text"
      placeholder="Search electronics..."
      value={searchTerm}
      onChange={(event) => setSearchTerm(event.target.value)}
      className="search-bar"
    />
  )
}

export default SearchBar