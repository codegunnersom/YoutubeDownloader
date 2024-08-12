const val MAX_EXPERIENCE : Int = 5000

fun main(args:Array<String>){
    val playerName : String = "Estragon"
    var experiencePoints : Int = 5
    var pubName : String = "Unicorn's Horn"
    var publicanName : String = "Ester"
    var playerGold : Int = 50
    experiencePoints += 5
    var hasSteed :Boolean = false
    println(playerName)
    println(experiencePoints)
    println("Has Steed : $hasSteed")
    println("Pub Name = $pubName")
    println("Publican's Name : $publicanName")
    println("$playerName has $playerGold Gold")
    println("$playerName's Name is reversed as : ${playerName.reversed()}")

    var playerRich = if (playerGold in 40..100){
        println("we rich")
    }
        else {
            println("We not rich")
        }

    var race = "gnome"

    val faction = when (race){
        "dwarf" -> "Keepers of the mine"
        "gnome" -> "keeps of the mine" 

        else -> {
            "some race"
        }
    }

    println(faction)



    }


