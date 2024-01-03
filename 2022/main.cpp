#include <memory>
#include <functional>
#include <iostream>

template<typename T>
class Serializer
{
    public:
    void serialize(T num)
    {
        serializeImpl<T>(num);
    }

    protected:
    template<typename W = T>
    void serializeImpl(W num, typename std::enable_if<!std::is_same<W, double>::value, void>::type* = nullptr)
    {
        std::cout << num << " not double";
    }
    template<typename W = T>
    void serializeImpl(W num, typename std::enable_if<std::is_same<W, double>::value, void>::type* = nullptr)
    {
        std::cout << num << " double";
    }
};

int main()
{
    auto ser = Serializer<int>();
    ser.serialize(2);
    return 0;
}
