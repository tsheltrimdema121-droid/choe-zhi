function scrollToProject() {
    const section = document.getElementById("project");

    section.scrollIntoView({ behavior: "smooth" });

    section.classList.add("highlight");

    setTimeout(() => {
        section.classList.remove("highlight");
    }, 2000);
}