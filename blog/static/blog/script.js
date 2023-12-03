document.addEventListener("DOMContentLoaded", () => {
    document.querySelector("#editBtn").onclick = function() {
        this.remove();

        const postTitleElement = document.querySelector("#postTitle");
        const postTitle = postTitleElement.innerHTML;
        postTitleElement.remove();
        console.log(postTitle);

        const postContentElement = document.querySelector("#postContent") ;
        const postContent = postContentElement.innerHTML;
        postContentElement.innerHTML = "";
        console.log(postContent);

        let titleInput = document.createElement("input");
        titleInput.setAttribute("type", "text");
        titleInput.className = "form-input form-control border border-primary mb-2";
        titleInput.name = "newTitle";
        titleInput.value = postTitle;

        let contentInput = document.createElement("textarea")
        contentInput.className = "form-input form-control border border-primary mb-2";
        contentInput.name = "newContent";
        contentInput.rows = 10;
        contentInput.value = postContent;

        let submitBtn = document.createElement("button");
        submitBtn.className = "btn btn-outline-primary my-2";
        submitBtn.innerHTML = "Editar";

        let postTitleDiv = document.querySelector("#postTitleDiv");
        postTitleDiv.append(titleInput);
        postContentElement.append(contentInput);
        postContentElement.append(submitBtn);
    }
})