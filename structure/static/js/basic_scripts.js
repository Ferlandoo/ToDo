// Message duration
window.onload = function () {
    setTimeout(function () {
        let element = document.getElementById('message-duration');
        if (element) {
            element.style.opacity = '0';
            element.style.transition = 'opacity 1s';

            setTimeout(function () {
                element.style.display = 'none';
            }, 1000);
        }
    }, 2500);
};

// Popup
const modal = document.querySelector('#popupTaskModal');
const openModalButtons = document.querySelectorAll('.popupTask');
const closeModalButton = document.querySelectorAll('.closePopupTask');
const taskTitle = modal.querySelector('.taskTitlePopup');
const taskContent = modal.querySelector('.taskContentPupup');
const deleteButton = document.querySelector('#deleteButton');

let currentTask = null;

openModalButtons.forEach(button => {
    button.addEventListener('click', () => {
        const task = {
            id: button.getAttribute('data-id'),
            title: button.getAttribute('data-title'),
            content: button.getAttribute('data-content'),
            color: button.getAttribute('data-color')
        };
        currentTask = task;
        if (modal && taskTitle && taskContent) {
            taskTitle.textContent = task.title;
            taskContent.textContent = task.content;
            taskTitle.classList.add(`bg-${task.color}-500`);
            modal.classList.remove('hidden');
            modal.classList.add('block');
        }
    });
});

if (deleteButton) {
    deleteButton.addEventListener('click', () => {
        if (currentTask) {
            window.location.href = `profile/delete/${currentTask.id}`;
        }
    });
}

closeModalButton.forEach(button => {
    button.addEventListener('click', () => {
        if (modal) {
            modal.classList.remove('block');
            modal.classList.add('hidden');
        }
    });
});

// Update Form
const modalUpdate = document.querySelector('#updateTaskModal');
const showModalUpdateButtons = document.querySelectorAll('.popupUpdateTask');
const closeModalUpdateButton = document.querySelectorAll('.closePopupUpdateTask');

showModalUpdateButtons.forEach(button => {
    button.addEventListener('click', () => {
        if (modalUpdate) {
            modalUpdate.classList.remove('hidden');
            modalUpdate.classList.add('block');
        }
    });
})
closeModalUpdateButton.forEach(button => {
    button.addEventListener('click', () => {
        if (modalUpdate) {
            modalUpdate.classList.remove('block');
            modalUpdate.classList.add('hidden');
        }
    });
});

// Get the elements
const popupTaskModal = document.querySelector('#popupTaskModal');
const updateTaskModal = document.querySelector('#updateTaskModal');
const updateButtonPopup = document.querySelector('#updateButtonPopup');

updateButtonPopup.addEventListener('click', () => {
    if (popupTaskModal) {
        popupTaskModal.classList.add('hidden');
    }
    if (updateTaskModal) {
        updateTaskModal.classList.remove('hidden');
    }
});
