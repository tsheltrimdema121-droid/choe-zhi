function scrollToProject() {
    const section = document.getElementById("project");

    section.scrollIntoView({ behavior: "smooth" });

    section.classList.add("highlight");

    setTimeout(() => {
        section.classList.remove("highlight");
    }, 2000);
function scrollToProject(){
document.getElementById("project")?.scrollIntoView({
behavior:"smooth"
});
function scrollToProject(){
    document.getElementById("project")?.scrollIntoView({
        behavior: "smooth"
    });
}

/* SIMPLE FADE LOAD */
window.onload = () => {
    document.querySelectorAll(".fade-in").forEach(el => {
        el.style.opacity = 1;
    });
};
}