  function deleteNote(mangaId) {
    fetch("/delete-manga", {
      method: "POST",
      body: JSON.stringify({ mangaId: mangaId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }