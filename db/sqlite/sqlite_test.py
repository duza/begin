# -*- coding:utf-8 -*-
# using python 2.7.3
#-------------------------
# Cookbook.py
# Created for Beginning Programming Using Python #8
# and Full Circle Magazine
#------------------------------------------------------
import apsw
import string
import webbrowser

class Cookbook:
    ''' '''
    def __init__(self):
        global connection
        global cursor
        self.totalcount = 0
        connection = apsw.Connection("cookbook1.db3")
        cursor = connection.cursor()

    def PrintAllRecipes(self):
        sql = 'SELECT * FROM Recipes'
        cntr = 0
        for x in cursor.execute(sql):
            cntr += 1
            print '%s %s %s %s' %(str(x[0]).rjust(5),x[1].ljust(30),x[2].ljust(20),x[3].ljust(30))
            print '-'*25
        self.totalcount = cntr

    def SearchForRecipe(self):
        print 'Please enter, what do you want to search:'
        print ' 1 - Search by recipe\'s name'
        print ' 2 - Search by its contain'
        print ' 3 - Search by word in the list of ingredients'
        print ' 4 - Return to main Menu'
        searchin = raw_input('Enter Search Type -> ')
        if searchin != '4':
            if searchin == '1':
                response = raw_input('Enter recipe\'s name ->')
                sql = "SELECT * FROM Recipes WHERE name LIKE '%s%%' " % response
                for x in cursor.execute(sql):
                    print '%s %s %s %s' %(str(x[0]).rjust(5),x[1].ljust(30),x[2].ljust(20),x[3].ljust(30))
            
            if searchin == '2':
                response = raw_input('Enter searchin content ->')
                sql = "SELECT Recipes.pkID, Recipes.name, Recipes.servings, Recipes.source, Instructions.instructions \
                FROM Recipes LEFT JOIN instructions ON (Recipes.pkID = Instructions.recipeid) \
                WHERE Instructions.instructions LIKE '%s%%' GROUP BY Recipes.pkID " % response 
                for x in cursor.execute(sql):
                    print '%s %s %s %s' %(str(x[0]).rjust(5),x[1].ljust(30),x[2].ljust(20),x[3].ljust(30),x[4].ljust(20))

            if searchin == '3':
                response = raw_input('Enter ingredient ->')
                sql = "SELECT Recipes.pkID, Recipes.name, Recipes.servings, Recipes.source, Ingredients.ingredients FROM Recipes LEFT JOIN ingredients ON (Recipes.pkID = Ingredients.recipeid) WHERE Ingredients.ingredients LIKE '%s%%' GROUP BY Recipes.pkID " % response
                for x in cursor.execute(sql):
                    print '%s %s %s %s' %(str(x[0]).rjust(5),str(x[1]).ljust(30),str(x[2]).ljust(20),str(x[3]).ljust(30),str(x[4]).ljust(20))           

    def PrintSingleRecipe(self,which):
        sql = 'SELECT * FROM Recipes WHERE pkID = %s' % str(which)
        for x in cursor.execute(sql):
            print '%s %s %s %s' % (str(x[0]).rjust(5),x[1].ljust(25),x[2].ljust(10),x[3].ljust(30))
        sql = 'SELECT * FROM Ingredients WHERE recipeID = %s' % str(which)
        for x in cursor.execute(sql):
            print u'Ингредиенты:\n%s' % x[1].rjust(len(x[1])+4)
        sql = 'SELECT * FROM Instructions WHERE recipeID = %s' % str(which)
        for x in cursor.execute(sql):
            print u'Рецепт:\n%s %s %s' % (str(x[0]).rjust(5),x[1].ljust(35),str(x[2]).ljust(5))

    def EnterNew(self):
        
        ings = []
        recipename, recipesource, recipeserves, instructions = '', '', '', ''
        lastid = 0
        resp = raw_input('Enter Recipe Title (Blank line to exit) -> ')
        if resp != '' :  # continue
            
            if string.find(resp,"'"):
                recipename = resp.replace("'","\'")
            else:
                recipename = resp
            print "RecipeName will be %s" % recipename
            
            resp = raw_input('Enter Recipe Source -> ')
            if string.find(resp,"'"):
                recipesource = resp.replace("'","\'")
            else:
                recipesource = resp
 
            resp = raw_input('Enter number of servings -> ')
            if string.find(resp,"'"):
                recipeserves = resp.replace("'","\'")
            else:
                recipeserves = resp
 
            print 'Now we will enter the ingredient list.'
            cont = True
            while cont == True:
                ing = raw_input('Enter Ingredient ("0" to exit) -> ')
                if ing != '0':
                    ings.append(ing)
                else:
                    cont = False

            resp = raw_input('Enter Instructions -> ')
            instructions = resp
            print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
            print "Here's what we have so far"
            print "Title: %s" % recipename
            print "Source: %s" % recipesource
            print "Serves: %s" % recipeserves
            print "Ingredients:"
            for x in ings:
                print x
            print "Instructions: %s" % instructions
            print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
            resp = raw_input("OK to save? (Y/N) -> ")
            if string.upper(resp) != 'N':
                # connection=apsw.Connection("cookbook1.db3")
                # cursor=connection.cursor()
                # Write the Recipe Record
                sql = 'INSERT INTO Recipes (name,servings,source) VALUES ("%s","%s","%s")' %(recipename,recipeserves,recipesource)
                cursor.execute(sql)
                # Get the new Recipe pkID
                sql = "SELECT last_insert_rowid()"
                cursor.execute(sql)
                for x in cursor.execute(sql):
                    lastid = x[0]
                    print "last id = %s" % lastid
                # Write the Instruction Record
                for x in ings:
                    sql = 'INSERT INTO Ingredients (recipeID,ingredients) VALUES (%s,"%s")' % (lastid,x)
                    cursor.execute(sql)
                # Write the Ingredients records
                sql = 'INSERT INTO Instructions (recipeID,instructions) VALUES( %s,"%s")' %(lastid,instructions)
                cursor.execute(sql)
                # Prompt the user that we are done
                print 'Done'
            else:
                print 'Save aborted'


    def DeleteRecipe(self,which):
        res = raw_input('Are you sure. Enter [Y or n] ->')
        if res.upper() == "Y":
            sql = "DELETE FROM Recipes WHERE pkID=%s" % which
            cursor.execute(sql)
            sql = "DELETE FROM Ingredients WHERE recipeID=%s" % which
            cursor.execute(sql)
            sql= "DELETE FROM Instructions WHERE recipeID=%s" % which
            cursor.execute(sql)

    def PrintOut(self,which):
        with open('fileprint.html','wb') as fi:
            sql = 'SELECT * FROM Recipes WHERE pkID = %s' % str(which)
            for x in cursor.execute(sql):
                fi.write(u'<h1> Name:%s</h1> <h2>Servings:%s</h2> <h2>Source:%s</h2>' % (x[1].ljust(25),x[2].ljust(10),x[3].ljust(30)))
            sql = 'SELECT * FROM Ingredients WHERE recipeID = %s' % str(which)
            fi.write('Ingredients:\n<ul>')
            for x in cursor.execute(sql):
                fi.write(u'<li>%s</li>' % x[1].rjust(len(x[1])+4))
            fi.write('</ul>')
            sql = 'SELECT * FROM Instructions WHERE recipeID = %s' % str(which)
            for x in cursor.execute(sql):
                fi.write(u'Instructions:\n%s' % (x[1].ljust(35)))
        webbrowser.open('fileprint.html')

def Menu():
    cbk = Cookbook() # Initialize the class
    loop = True
    while loop == True:
        print '='*79
        print '               RECIPE DATABASE'
        print '='*79
        print ' 1 - Show All Recipes'
        print ' 2 - Search for a recipe'
        print ' 3 - Show a Recipe'
        print ' 4 - Delete a recipe'
        print ' 5 - Add a recipe'
        print ' 6 - Print a recipe'
        print ' 0 - Exit'
        print '='*79
        response = raw_input('Enter a selection -> ')
        if response == '1': # Show all recipes
            cbk.PrintAllRecipes()
            print 'Total Recipes - %s' %cbk.totalcount
            print '-'*35
            res = raw_input('Press A Key -> ')

        elif response == '2': # Search for a recipe
            cbk.SearchForRecipe()
        elif response == '3': # Show a single recipe
            cbk.PrintAllRecipes()
            try:
                id_recipe = raw_input('Select a recipe ->')
                cbk.PrintSingleRecipe(id_recipe)
            except ValueError as error:
                print error
            except Exception as e:
                print 'Unexcepted error!',e
        elif response == '4': # Delete Recipe
            delrecipeid = raw_input('What recipe need delete? Its id ->')
            cbk.DeleteRecipe(delrecipeid)
        elif response == '5': # Add a recipe
            try:
                cbk.EnterNew()
            except Exception as eee:
                print eee
        elif response == '6': # Print a recipe
            cbk.PrintAllRecipes()
            printrecipeid = raw_input('What recipe need print? Its id ->')
            cbk.PrintOut(printrecipeid)
        elif response == '0': # Exit the program
            print 'Goodbye'
            loop = False
        else:
            print 'Unrecognized command.  Try again.' 

def main():
    Menu()

if __name__ == '__main__':
    main()