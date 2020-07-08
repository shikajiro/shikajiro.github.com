Title: Androidで現在起動中のActivityを知る方法
Date: 2020-07-08 22:36
Modified: 2020-07-08 22:36
Category: Android
Tags: Android, debug
Slug: current-activity
Authors: Shikajiro

Android開発にて Activity, Fragment での画面遷移が入り乱れる実装をしていると、現在動かしている画面のActivityが何なのか知りたくなることがある。

昔の LayoutInspector や adb でも調べることができるけど、ログに出力する方法を書き残す。

ActivityLifecycleCallbacks を使って、activityがアクティブになった段階でログを出力すれば良い。

```kotlin
class MainApplication : Application() {

    private val activityLifecycleCallbacks = object : ActivityLifecycleCallbacks {

        override fun onActivityCreated(activity: Activity, bundle: Bundle?) {}

        override fun onActivityStarted(activity: Activity) {}

        override fun onActivityResumed(activity: Activity) {
            Timber.i("current activity is $activity")
        }

        override fun onActivityPaused(activity: Activity) {}

        override fun onActivityStopped(activity: Activity) {}

        override fun onActivitySaveInstanceState(activity: Activity, bundle: Bundle?) {}

        override fun onActivityDestroyed(activity: Activity) {}
    }

    override fun onCreate() {
        registerActivityLifecycleCallbacks(activityLifecycleCallbacks)
    }

}
```

こんな感じでログに出る
```
$ adb logcat  "*:D" | grep "current activity"
2020-07-08 22:00:44.313 18192-18192/com.shikajiro.app D/MainApplication$activityLifecycleCallbacks: current activity is com.shikajiro.app.presentation.splash.SplashActivity@9247039
2020-07-08 22:00:47.595 18192-18192/com.shikajiro.app D/MainApplication$activityLifecycleCallbacks: current activity is com.shikajiro.app.presentation.login.LoginActivity@6a682f8
2020-07-08 22:05:44.506 18956-18956/com.shikajiro.app D/MainApplication$activityLifecycleCallbacks: current activity is com.shikajiro.app.presentation.tutorial.TutorialActivity@be0b6ac
2020-07-08 22:05:44.506 18956-18956/com.shikajiro.app D/MainApplication$activityLifecycleCallbacks: current activity is com.shikajiro.app.presentation.main.MainActivity@4aba5c5
```