// Popup
function toggleTaskModal(taskId, action) {
    const modal = document.querySelector(`#popupTaskModal-${taskId}`);
    if (modal) {
        if (action === 'show') {
            modal.classList.remove('hidden');
            modal.classList.add('block');
        } else if (action === 'hide') {
            modal.classList.remove('block');
            modal.classList.add('hidden');
        }
    }
}

const showTaskModalButtons = document.querySelectorAll('.popupTask');
showTaskModalButtons.forEach(button => {
    button.addEventListener('click', function () {
        const taskId = this.getAttribute('data-task-id');
        toggleTaskModal(taskId, 'show');
    });
});

const closeTaskModalButtons = document.querySelectorAll('.closePopupTask');
closeTaskModalButtons.forEach(button => {
    button.addEventListener('click', function () {
        const taskId = this.getAttribute('data-task-id');
        toggleTaskModal(taskId, 'hide');
    });
});

// Update Form
function toggleModal(taskId, action) {
    const modal = document.querySelector(`#updateTaskModal-${taskId}`);
    if (modal) {
        if (action === 'show') {
            modal.classList.remove('hidden');
            modal.classList.add('block');
        } else if (action === 'hide') {
            modal.classList.remove('block');
            modal.classList.add('hidden');
        }
    }
}

const showModalUpdateButtons = document.querySelectorAll('.popupUpdateTask');
showModalUpdateButtons.forEach(button => {
    button.addEventListener('click', function () {
        const taskId = this.getAttribute('data-task-id');
        toggleModal(taskId, 'show');
    });
});

const closeModalUpdateButtons = document.querySelectorAll('.closePopupUpdateTask');
closeModalUpdateButtons.forEach(button => {
    button.addEventListener('click', function () {
        const taskId = this.getAttribute('data-task-id');
        toggleModal(taskId, 'hide');
    });
});

// Get the elements
const showUpdateModalButtons = document.querySelectorAll('.popupUpdateTask');
showUpdateModalButtons.forEach(button => {
    button.addEventListener('click', function () {
        const taskId = this.getAttribute('data-task-id');
        toggleModal(taskId, 'show');
    });
});
