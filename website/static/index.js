function deleteNote(noteId) {
  const payload = {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      noteId: noteId,
    }),
  };
  fetch("/delete-note", payload).then((_res) => {
    window.location.href = "/";
  });
}
