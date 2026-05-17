describe('beforeEach — todos', () => {
    let uid // user id
    let name // name of the user (firstName + ' ' + lastName)
    let email // email of the user
//eiHqkDoFFFU
    before(function () {
    // create a fabricated user from a fixture
    cy.fixture('user.json')
      .then((user) => {
        cy.request({
          method: 'POST',
          url: 'http://localhost:5000/users/create',
          form: true,
          body: user
        }).then((response) => {
          uid = response.body._id.$oid
          name = user.firstName + ' ' + user.lastName
          email = user.email
        })
      }).then(() => {
        console.log("uid")
        console.log(uid)
        cy.fixture('task.json').then((tasks) => {
                        tasks.userid = uid;

                        cy.request({
                            method: 'POST',
                            url: 'http://localhost:5000/tasks/create',
                            form: true,
                            body: tasks
                        })
                    })
      })
  })
  /*beforeEach(() => {
    cy.visit('http://localhost:3000')
    cy.contains('div', 'Email Address').find('input[type=text]').type(email)
    cy.get('form').submit()
    cy.get('[id="title"]').type('chase')
    cy.get('[id="url"]').type('eiHqkDoFFFU')
    cy.get('form').submit()
    cy.get('a')
  })
  afterEach(() => {

  })*/

  it('can be appended to the end of the task todo list', () => {
    //cy.get('.new-todo').type('Buy milk{enter}')
    //cy.get('.new-todo').type('Read a book{enter}')
    //cy.get('.new-todo').type('Go for a walk{enter}')
  })
})