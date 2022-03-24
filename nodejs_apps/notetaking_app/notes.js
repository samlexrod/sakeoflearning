const fs = require('fs')
const chalk = require('chalk')

// Create remove command
const removeNote = (title) => {
    const notes = loadNotes()
    const noteIndex = notes.findIndex((note) => note.title === title)

    if (noteIndex > -1) {
        notes.splice(noteIndex, 1)
        saveNotes(notes)
        console.log(chalk.green.inverse('Note removed!'))
    } else {
        console.log(chalk.red.inverse('Note not found!'))
    }
}

// Create list command
const listNotes = () => {
    const notes = loadNotes()
    console.log(chalk.inverse('Your notes:'))
    notes.forEach((note) => {
        console.log(note.title)
    }
    )
}

// Create read command
const readNote = (title) => {
    const notes = loadNotes()
    const note = notes.find((note) => note.title === title)
    if (note) {
        console.log(chalk.inverse(note.body))
    } else {
        console.log(chalk.red.inverse('Note not found!'))
    }
}

    
// Create add command
const addNote = (title, body) => {
    const notes = loadNotes()
    const duplicateNotes = notes.find((note) => note.title === title)
    console.log(duplicateNotes)
    if (!duplicateNotes) {
        notes.push({
            title: title,
            body: body
        })
        saveNotes(notes)
        return true
    } else {
        console.log(chalk.red.inverse('Note title taken'))
    }
}

// Create save command
const saveNotes = (notes) => {
    const dataJSON = JSON.stringify(notes)
    fs.writeFileSync('notes.json', dataJSON)
}

// Create load command
const loadNotes = () => {       
    try {
        const dataBuffer = fs.readFileSync('notes.json')
        const dataJSON = dataBuffer.toString()
        return JSON.parse(dataJSON)
    } catch (e) {
        return []
    }
}

module.exports = {
    addNote: addNote,
    removeNote: removeNote,
    listNotes: listNotes,
    readNote: readNote
}