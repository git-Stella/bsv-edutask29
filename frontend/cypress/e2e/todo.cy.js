describe('beforeEach — todos', () => {
    let uid // user id
    let name // name of the user (firstName + ' ' + lastName)
    let email // email of the user
//eiHqkDoFFFU
    before(function () {
    // create a fabricated user from a fixture
    /*cy.fixture('user.json')
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
      })*/
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
        /*cy.visit('http://localhost:3000')
        cy.contains('div', 'Email Address').find('input[type=text]').type(email)
        cy.get('form').submit()
        cy.get('[id="title"]').type('chase')
        cy.get('[id="url"]').type('eiHqkDoFFFU')
        cy.get('form').submit()*/
        //cy.get('a').last().click()
      }).then(() => {
        //cy.get('a').last().click()
      })
    //cy.visit('http://localhost:3000')
  })
  beforeEach(() => {
    cy.visit('http://localhost:3000')
    cy.contains('div', 'Email Address').find('input[type=text]').type(email)
    cy.get('form').submit()
    cy.get('[id="title"]').type('chase')
    cy.get('[id="url"]').type('eiHqkDoFFFU')
    cy.get('form').submit()
    cy.get('a').last().click()
  })

  it('can be appended to the end of the task todo list', () => {
    cy.get('[placeholder="Add a new todo item"]').type('Buy milk{enter}')
    //cy.get('form').submit()
    cy.get('[class="todo-item"]').last().contains('Buy milk')//find('span[class=checker]').check()
  })

  it('can not append todo if there is no text', () => {
    cy.get('form').submit()
    cy.get('[class="todo-item"]').last().contains('Watch video')
  })

  it('can check and uncheck elements', () => {
    //could split this into separate tests?
    cy.get('[class="todo-item"]').find('[class="checker unchecked"]').click()
    cy.get('[class="todo-item"]').find('[class="checker checked"]').click()
  })

  it('can remove a todo item', () => {
    cy.get('[class="todo-item"]').find('[class="remover"]').click()
  })

  /*after(() => {

  })*/
  after(function () {
    // clean up by deleting the user from the database
    cy.request({
      method: 'DELETE',
      url: `http://localhost:5000/users/${uid}`
    }).then((response) => {
      cy.log(response.body)
    })
  })
})